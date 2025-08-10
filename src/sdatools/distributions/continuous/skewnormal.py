from math import sqrt, pi
from scipy.stats import skewnorm

from sdatools.core.functions import phi, Phi
from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class SkewNormalDistribution(ContinuousDistribution):
    """
    A class representing a skew-normal distribution with location xi, scale omega, and shape alpha
    """
    
    def __init__(self, xi: float = 0.0, omega: float = 1.0, alpha: float = 0.0):  
        if omega <= 0:
            raise ValueError("Scale parameter omega must be positive.")
        self._xi = xi
        self._omega = omega
        self._alpha = alpha

        self._delta = alpha / sqrt(1 + alpha ** 2)

    # Special methods

    def __repr__(self) -> str:
        return f"SkewNormalDistribution(xi={self._xi}, omega={self._omega}, alpha={self._alpha})"    

    def __str__(self) -> str:
        return f"SN({self._xi}, {self._omega}, {self._alpha})"
    
    def __hash__(self) -> int:
        return hash((self._xi, self._omega, self._alpha))
    
    # Distribution parameters

    @property
    def xi(self) -> float:
        return self._xi
    
    @property
    def omega(self) -> float:
        return self._omega
    
    @property
    def alpha(self) -> float:
        return self._alpha
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    
    # Moments
    
    @property
    def mean(self) -> float:
        return self._xi + (self._omega * sqrt(2 / pi) * self._delta)

    @property
    def variance(self) -> float:
        return (self._omega ** 2) * (1 - (2 * self._delta ** 2) / pi)
    
    @property
    def skewness(self) -> float:
        return (4 - pi) / 2 * (self._delta * sqrt(2 / pi)) ** 3 / ((1 - 2 * self._delta ** 2 / pi) ** (3/2))
    
    @property
    def kurtosis(self) -> float:
        return 2 * (pi - 3) * (self._delta * sqrt(2 / pi)) ** 4 / ((1 - 2 * self._delta ** 2 / pi) ** 2)
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        z = (x - self._xi) / self._omega
        return 2 / self._omega * phi(z) * Phi(self._alpha * z)
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        # TODO: Implement without scipy
        return float(skewnorm.cdf(x, self._alpha, loc=self._xi, scale=self._omega))
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement SkewNormal inverse CDF
        raise NotImplementedError("Inverse CDF for SkewNormalDistribution is not implemented yet.")
    
    # Sampling
    
    def sample(self, size: int = 1) -> list[float]:
        """
        Generate n samples (n = size) from the SkewNormal distribution
        """
        # TODO: Implement manually using Box-Muller transform or similar method
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        raise NotImplementedError("Sampling from SkewNormalDistribution is not implemented yet.")
        # return skewnorm.rvs(self.alpha, loc=self.xi, scale=self.omega, size=size).tolist()
    