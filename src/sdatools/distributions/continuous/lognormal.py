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
        self.mu = mu
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        self.sigma = sigma

    # Special methods

    def __repr__(self) -> str:
        return f"LognormalDistribution(mu={self.mu}, sigma={self.sigma})"    

    def __str__(self) -> str:
        return f"Lognormal({self.mu}, {self.sigma ** 2})"
    
    def __hash__(self) -> int:
        return hash((self.mu, self.sigma))

    def __mul__(self, scalar) -> 'LogNormalDistribution':
        """
        Left multiplication to allow LognormalDistribution * scalar

        If ln(X) ~ N(mu, sigma**2) and c > 0, then c * ln(X) ~ N(mu + ln(c), sigma**2)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        return LogNormalDistribution(self.mu + scalar, self.sigma)
    
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
        return LogNormalDistribution(self.mu - scalar, self.sigma)
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [0, float('inf')] # TODO: How to represent open interval in Python?
    
    # Moments
    
    @property
    def mean(self) -> float:
        return exp(self.mu + self.sigma ** 2 / 2)

    @property
    def variance(self) -> float:
        return (exp(self.sigma ** 2) - 1) * exp(2 * self.mu + self.sigma ** 2)
    
    @property
    def skewness(self) -> float:
        return (exp(self.sigma ** 2) + 2) * sqrt(exp(self.sigma ** 2) - 1)
    
    @property
    def kurtosis(self) -> float:
        return exp(4 * self.sigma ** 2) + 2 * exp(3 * self.sigma ** 2) + 3 * exp(2 * self.sigma ** 2) - 6
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return (1.0 / (x * self.sigma * sqrt(2.0 * pi))) * exp(-((np.log(x) - self.mu) ** 2) / (2.0 * self.sigma ** 2))
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        if x <= 0:
            return 0.0
        return Phi((np.log(x) - self.mu) / self.sigma)
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement without using scipy for educational purposes
        return float(lognorm.ppf(p, loc=self.mu, scale=self.sigma))
    
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
        return np.random.lognormal(mean=self.mu, sigma=self.sigma, size=size).tolist()
    