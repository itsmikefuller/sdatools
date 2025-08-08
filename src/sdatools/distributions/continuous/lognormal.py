from math import exp, sqrt, pi
import numpy as np
from scipy.stats import lognorm

from sdatools.core.functions import Phi
from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class LogNormalDistribution(ContinuousDistribution):
    """
    A class representing a lognormal distribution with mean mu and standard deviation sigma
    
    Note: a LognormalDistribution(mu, sigma) object relates to the random variable ln(X) ~ N(mu, sigma**2)
    """
    
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):  
        if sigma <= 0:
            raise ValueError("Standard deviation, sigma, must be positive.")
        self._mu = mu
        self._sigma = sigma

    # Special methods

    def __repr__(self) -> str:
        return f"LognormalDistribution(mu={self._mu}, sigma={self._sigma})"    

    def __str__(self) -> str:
        return f"Lognormal({self._mu}, {self._sigma ** 2})"
    
    def __hash__(self) -> int:
        return hash((self._mu, self._sigma))

    def __mul__(self, scalar) -> 'LogNormalDistribution':
        """
        Left multiplication to allow LognormalDistribution * scalar

        If ln(X) ~ N(mu, sigma**2) and c > 0, then c * ln(X) ~ N(mu + ln(c), sigma**2)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        return LogNormalDistribution(self._mu + scalar, self._sigma)
    
    def __rmul__(self, other):
        """
        Right multiplication to allow scalar * NormalDistribution
        """
        return self.__mul__(other)

    def __truediv__(self, scalar) -> 'LogNormalDistribution':
        """
        Divide the normal distribution by a scalar

        If ln(X) ~ N(mu, sigma**2) and c > 0, then ln(X) / c ~ N(mu - ln(c), sigma**2)
        """
        if not isinstance(scalar, (int, float)) or scalar == 0:
            raise ValueError("Can only divide by a non-zero scalar (int or float).")
        return LogNormalDistribution(self._mu - scalar, self._sigma)
    
    # Distribution parameters

    @property
    def mu(self) -> float:
        return self._mu
    
    @property
    def sigma(self) -> float:
        return self._sigma
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [0, float('inf')] # TODO: How to represent open interval in Python?
    
    # Moments
    
    @property
    def mean(self) -> float:
        return exp(self._mu + self._sigma ** 2 / 2)

    @property
    def variance(self) -> float:
        return (exp(self._sigma ** 2) - 1) * exp(2 * self._mu + self._sigma ** 2)
    
    @property
    def skewness(self) -> float:
        return (exp(self._sigma ** 2) + 2) * sqrt(exp(self._sigma ** 2) - 1)
    
    @property
    def kurtosis(self) -> float:
        return exp(4 * self._sigma ** 2) + 2 * exp(3 * self._sigma ** 2) + 3 * exp(2 * self._sigma ** 2) - 6
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return (1.0 / (x * self._sigma * sqrt(2.0 * pi))) * exp(-((np.log(x) - self._mu) ** 2) / (2.0 * self._sigma ** 2))
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return Phi((np.log(x) - self._mu) / self._sigma)
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement without using scipy for educational purposes
        return float(lognorm.ppf(p, loc=self._mu, scale=self._sigma))
    
    # Sampling
    
    def sample(self, size: int = 1) -> list[float]:
        """
        Generate n samples (n = size) from the Normal distribution
        """
        # TODO: Implement manually using Box-Muller transform or similar method
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        return np.random.lognormal(mean=self._mu, sigma=self._sigma, size=size).tolist()
    