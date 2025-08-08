from math import sqrt
import numpy as np
from scipy.stats import norm

from sdatools.core.functions import phi, Phi
from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class NormalDistribution(ContinuousDistribution):
    """
    A class representing a normal distribution with mean mu and standard deviation sigma
    
    Note: a NormalDistribution(mu, sigma) object relates to the random variable X ~ N(mu, sigma**2)
    """
    
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):  
        self.mu = mu
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        self.sigma = sigma

    # Special methods

    def __repr__(self) -> str:
        return f"NormalDistribution(mu={self.mu}, sigma={self.sigma})"    

    def __str__(self) -> str:
        return f"N({self.mu}, {self.sigma ** 2})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NormalDistribution):
            return NotImplemented
        return self.mu == other.mu and self.sigma == other.sigma    

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, NormalDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.mu, self.sigma))

    def __add__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """
        Add two normal distributions

        If X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then X + Y ~ N(mu1 + mu2, sqrt(sigma1^2 + sigma2^2))
        """
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only add another NormalDistribution.")
        new_mu = self.mu + other.mu
        new_sigma = sqrt(self.sigma ** 2 + other.sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)
    
    def __sub__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """
        Subtract two normal distributions

        If X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then X - Y ~ N(mu1 - mu2, sqrt(sigma1^2 + sigma2^2))
        """
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only subtract another NormalDistribution.")
        new_mu = self.mu - other.mu
        new_sigma = sqrt(self.sigma ** 2 + other.sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)

    def __mul__(self, scalar) -> 'NormalDistribution':
        """
        Left multiplication to allow NormalDistribution * scalar

        If X ~ N(mu, sigma) and c in R, then c * X ~ N(c * mu, |c| * sigma)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        new_mu = scalar * self.mu
        new_sigma = abs(scalar) * self.sigma
        return NormalDistribution(new_mu, new_sigma)
    
    def __rmul__(self, other):
        """
        Right multiplication to allow scalar * NormalDistribution
        """
        return self.__mul__(other)

    def __truediv__(self, scalar) -> 'NormalDistribution':
        """
        Divide the normal distribution by a scalar

        If X ~ N(mu, sigma) and c != 0, then X / c ~ N(mu / c, sigma / |c|)
        """
        if not isinstance(scalar, (int, float)) or scalar == 0:
            raise ValueError("Can only divide by a non-zero scalar (int or float).")
        new_mu = self.mu / scalar
        new_sigma = self.sigma / abs(scalar)
        return NormalDistribution(new_mu, new_sigma)
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    
    # Moments
    
    @property
    def mean(self) -> float:
        return self.mu

    @property
    def variance(self) -> float:
        return self.sigma ** 2
    
    @property
    def skewness(self) -> float:
        return 0.0
    
    @property
    def kurtosis(self) -> float:
        return 0.0
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        return phi((x - self.mu) / self.sigma) / self.sigma
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        return Phi((x - self.mu) / self.sigma)
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement without using scipy for educational purposes
        return float(norm.ppf(p, loc=self.mu, scale=self.sigma))
    
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
        return np.random.normal(loc=self.mu, scale=self.sigma, size=size).tolist()
    