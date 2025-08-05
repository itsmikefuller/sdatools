import numpy as np
import pandas as pd

from sdatools.distributions.base_distribution import Distribution

from sdatools.distributions.continuous.normal import NormalDistribution
from sdatools.distributions.continuous.lognormal import LognormalDistribution
from sdatools.distributions.continuous.gamma import GammaDistribution
from sdatools.distributions.continuous.exponential import ExponentialDistribution
from sdatools.distributions.continuous.skewnormal import SkewNormalDistribution


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
                 data: list[float] | np.ndarray | pd.Series,
                 order: int = 4):
        self.data: np.ndarray = np.asarray(data)
        self.calculate_sample_moments(order=order)
        self.fitting_methods: dict = {
            NormalDistribution: self._fit_normal,
            GammaDistribution: self._fit_gamma,
            ExponentialDistribution: self._fit_exponential,
            LognormalDistribution: self._fit_lognormal,
            SkewNormalDistribution: self._fit_skew_normal
        }


    def calculate_sample_moments(self, order: int = 4):
        """
        Calculates the sample moments of the data

        Args:
            order (int): The number of moments to calculate (default is 4)

        Returns:
            tuple: A tuple containing mean, variance, skewness, and kurtosis
        """
        self.n: int = len(self.data)
        if self.n < 2:
            raise ValueError("Cannot calculate sample moments - at least two data points are required.")
        if any(np.isnan(self.data)):
            raise ValueError("Cannot calculate sample moments - data contains NaNs.")
        self.mean: float = sum(self.data) / self.n
        self.variance: float = sum((x - self.mean) ** 2 for x in self.data) / self.n

        if order >= 3:
            if self.n < 3:
                raise ValueError("At least three data points are required to calculate skewness.")
            if self.variance == 0:
                raise ValueError("Variance is zero, cannot calculate skewness and kurtosis.")
            self.skewness: float = sum((x - self.mean) ** 3 for x in self.data) / (self.n * (self.variance ** 1.5))
        
        if order >= 4:
            if self.n < 4:
                raise ValueError("At least four data points are required to calculate kurtosis.")
            self.kurtosis: float = sum((x - self.mean) ** 4 for x in self.data) / (self.n * (self.variance ** 2)) - 3


    def fit(self, dist: type[Distribution] | Distribution) -> Distribution:
        """
        Estimates the parameters of the distribution using the Method of Moments

        Args:
            dist_type (type[Distribution] or Distribution): The distribution type to fit, e.g. NormalDistribution, GammaDistribution

        Returns:
            Distribution: The fitted distribution with estimated parameters
        """
        dist_type = dist if isinstance(dist, type) else type(dist)
        if dist_type not in self.fitting_methods:
            raise NotImplementedError(f"Method of Moments fitting not implemented for {dist_type.__name__}")
        return self.fitting_methods[dist_type]()


    # Fitting methods for specific distributions

    def _fit_normal(self) -> NormalDistribution:
        mu = self.mean
        sigma = self.variance ** 0.5
        return NormalDistribution(mu=mu, sigma=sigma)


    def _fit_gamma(self) -> GammaDistribution:
        alpha = self.mean ** 2 / self.variance
        beta = self.variance / self.mean
        return GammaDistribution(alpha=alpha, beta=beta)


    def _fit_exponential(self) -> ExponentialDistribution:
        lam = 1 / self.mean
        return ExponentialDistribution(lam=lam)


    def _fit_lognormal(self) -> LognormalDistribution:
        mu = np.log(self.mean ** 2 / (self.variance + self.mean ** 2))
        sigma = np.sqrt(np.log(1 + (self.variance / self.mean ** 2)))
        return LognormalDistribution(mu=mu, sigma=sigma)
    
    
    def _fit_skew_normal(self) -> SkewNormalDistribution:
        delta = self.skewness / np.sqrt(1 + self.skewness ** 2)**(1/3)
        alpha = delta / np.sqrt(1 - delta**2)
        omega = np.sqrt(self.variance * (1 - 2 * delta**2 / np.pi))
        xi = self.mean - (omega * np.sqrt(2 / np.pi) * alpha / np.sqrt(1 + alpha ** 2))
        return SkewNormalDistribution(xi=xi, omega=omega, alpha=alpha)
    