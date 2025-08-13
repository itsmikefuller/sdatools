from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar
import numpy as np

from sdatools.core.types import SeriesLike
from sdatools.distributions.abstract.distribution import Distribution

if TYPE_CHECKING:
    from sdatools.distributions.continuous.normal import NormalDistribution
    from sdatools.distributions.continuous.gamma import GammaDistribution
    from sdatools.distributions.continuous.exponential import ExponentialDistribution
    from sdatools.distributions.continuous.lognormal import LogNormalDistribution
    from sdatools.distributions.continuous.skewnormal import SkewNormalDistribution

T = TypeVar("T", bound=Distribution)


class MethodOfMoments:
    """
    A class to perform parameter estimation using the Method of Moments

    Inputs:
        data (list[float], np.ndarray or pd.Series): A list of observed data points
        order (int): The number of moments to calculate (default is 4)

    Methods:
        calculate_moments(): Calculates the sample moments of the data
        fit(): Estimates the parameters of the distribution using the method of moments
    """

    def __init__(self, 
                 data: SeriesLike,
                 order: int = 4):
        self._data: np.ndarray = np.asarray(data)
        self._n: int = len(self._data)
        self._order: int = order
        self._calculate_sample_moments(order=order)
        self._fitting_methods: dict = {
            "NormalDistribution": self._fit_normal,
            "GammaDistribution": self._fit_gamma,
            "ExponentialDistribution": self._fit_exponential,
            "LogNormalDistribution": self._fit_lognormal,
            "SkewNormalDistribution": self._fit_skew_normal
        }


    def _calculate_sample_moments(self, order: int = 4):
        """
        Calculates the sample moments of the data

        Args:
            order (int): The number of moments to calculate (default is 4)

        Returns:
            tuple: A tuple containing mean, variance, skewness, and kurtosis
        """
        
        if self._n < 2:
            raise ValueError("Cannot calculate sample moments - at least two data points are required.")
        if any(np.isnan(self._data)):
            raise ValueError("Cannot calculate sample moments - data contains NaNs.")
        self.sample_mean: float = sum(self._data) / self._n
        self.sample_variance: float = sum((x - self.sample_mean) ** 2 for x in self._data) / self._n

        if self._order >= 3:
            if self._n < 3:
                raise ValueError("At least three data points are required to calculate skewness.")
            if self.sample_variance == 0:
                raise ValueError("Variance is zero, cannot calculate skewness and kurtosis.")
            self.sample_skewness: float = sum((x - self.sample_mean) ** 3 for x in self._data) / (self._n * (self.sample_variance ** 1.5))
        
        if self._order >= 4:
            if self._n < 4:
                raise ValueError("At least four data points are required to calculate kurtosis.")
            self.sample_kurtosis: float = sum((x - self.sample_mean) ** 4 for x in self._data) / (self._n * (self.sample_variance ** 2)) - 3


    def fit(self, dist: type[T] | T) -> T:
        """
        Estimates the parameters of a given distribution (dist) using the Method of Moments.

        Args:
            dist (Type[T] or T): A distribution class or an instance of it.
                Must be one of:
                - NormalDistribution
                - GammaDistribution
                - ExponentialDistribution
                - LogNormalDistribution
                - SkewNormalDistribution

        Returns:
            T: A fitted instance of the same distribution type, with parameters estimated from the data.
        """
        dist_type: type[T] = dist if isinstance(dist, type) else type(dist)
        dist_name: str = dist_type.__name__
        if dist_name not in self._fitting_methods:
            raise NotImplementedError(f"Method of Moments fitting not implemented for {dist_name}")
        return self._fitting_methods[dist_name]()


    # Fitting methods for specific distributions

    def _fit_normal(self) -> NormalDistribution:
        from sdatools.distributions.continuous.normal import NormalDistribution
        mu = self.sample_mean
        sigma = self.sample_variance ** 0.5
        return NormalDistribution(mu=mu, sigma=sigma)


    def _fit_gamma(self) -> GammaDistribution:
        from sdatools.distributions.continuous.gamma import GammaDistribution
        alpha = self.sample_mean ** 2 / self.sample_variance
        beta = self.sample_variance / self.sample_mean
        return GammaDistribution(alpha=alpha, beta=beta)


    def _fit_exponential(self) -> ExponentialDistribution:
        from sdatools.distributions.continuous.exponential import ExponentialDistribution
        lam = 1 / self.sample_mean
        return ExponentialDistribution(lam=lam)


    def _fit_lognormal(self) -> LogNormalDistribution:
        from sdatools.distributions.continuous.lognormal import LogNormalDistribution
        mu = np.log(self.sample_mean ** 2 / (self.sample_variance + self.sample_mean ** 2))
        sigma = np.sqrt(np.log(1 + (self.sample_variance / self.sample_mean ** 2)))
        return LogNormalDistribution(mu=mu, sigma=sigma)
    
    
    def _fit_skew_normal(self) -> SkewNormalDistribution:
        from sdatools.distributions.continuous.skewnormal import SkewNormalDistribution
        delta = self.sample_skewness / np.sqrt(1 + self.sample_skewness ** 2)**(1/3)
        alpha = delta / np.sqrt(1 - delta**2)
        omega = np.sqrt(self.sample_variance * (1 - 2 * delta**2 / np.pi))
        xi = self.sample_mean - (omega * np.sqrt(2 / np.pi) * alpha / np.sqrt(1 + alpha ** 2))
        return SkewNormalDistribution(xi=xi, omega=omega, alpha=alpha)
    