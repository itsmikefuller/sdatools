from sdatools.distributions.continuous.continuous_distribution import ContinuousDistribution

import numpy as np


class UniformDistribution(ContinuousDistribution):
    '''A class representing a Uniform distribution on the interval [a, b].

    Note: a UniformDistribution(a, b) object relates to the random variable X ~ U(a, b).'''
    def __init__(self, a: float = 0.0, b: float = 1.0):
        if a >= b:
            raise ValueError("Lower bound 'a' must be less than upper bound 'b'.")
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        """String representation of the uniform distribution."""
        return f"UniformDistribution(a={self.a}, b={self.b})"
    
    def __str__(self) -> str:
        """String representation of the uniform distribution."""
        return f"U({self.a}, {self.b})"
    
    def __eq__(self, other: object) -> bool:
        """Check equality of two uniform distributions."""
        if not isinstance(other, UniformDistribution):
            return NotImplemented
        return self.a == other.a and self.b == other.b
    
    def __ne__(self, other: object) -> bool:
        """Check inequality of two uniform distributions."""
        if not isinstance(other, UniformDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        """Return a hash value for the uniform distribution."""
        return hash((self.a, self.b))
    
    def pdf(self, x: float) -> float:
        """Probability density function for the uniform distribution."""
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        else:
            return 0.0
        
    def cdf(self, x: float) -> float:
        """Cumulative distribution function for the uniform distribution."""
        if x < self.a:
            return 0.0
        elif x > self.b:
            return 1.0
        else:
            return (x - self.a) / (self.b - self.a)
        
    def mean(self) -> float:
        """Mean of the uniform distribution."""
        return (self.a + self.b) / 2
    
    def variance(self) -> float:
        """Variance of the uniform distribution."""
        return (self.b - self.a) ** 2 / 12
    
    def skewness(self) -> float:
        """Skewness of the uniform distribution."""
        return 0.0
    
    def kurtosis(self) -> float:
        """Kurtosis of the uniform distribution."""
        return 1.8

    def domain(self) -> list[float]:
        """Domain of the uniform distribution."""
        return [self.a, self.b]
    
    def sample(self, size: int = 1) -> list[float]:
        """Generate a sample of size `size` from the uniform distribution."""
        # TODO: Implement sample method for uniform distribution manually
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        return np.random.uniform(low=self.a, high=self.b, size=size).tolist()
    
    def inverse_cdf(self, p: float) -> float:
        """Calculate the quantile function (inverse CDF) for the uniform distribution."""
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be in the range [0, 1].")
        return self.a + p * (self.b - self.a)
    
