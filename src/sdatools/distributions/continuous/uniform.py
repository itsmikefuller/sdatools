import numpy as np

from sdatools.distributions import ContinuousDistribution


class UniformDistribution(ContinuousDistribution):
    """
    A class representing a Uniform distribution on the interval [a, b]
    """
    def __init__(self, a: float = 0.0, b: float = 1.0):
        if a >= b:
            raise ValueError("Lower bound 'a' must be less than upper bound 'b'.")
        self.a = a
        self.b = b

    # Special methods

    def __repr__(self) -> str:
        return f"UniformDistribution(a={self.a}, b={self.b})"
    
    def __str__(self) -> str:
        return f"U({self.a}, {self.b})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UniformDistribution):
            return NotImplemented
        return self.a == other.a and self.b == other.b
    
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, UniformDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.a, self.b))
    
    # Domain

    def domain(self) -> list[float]:
        return [self.a, self.b]

    # Moments
   
    def mean(self) -> float:
        return (self.a + self.b) / 2
    
    def variance(self) -> float:
        return (self.b - self.a) ** 2 / 12
    
    def skewness(self) -> float:
        return 0.0
    
    def kurtosis(self) -> float:
        return -1.2

    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        else:
            return 0.0

    # @vectorise_input    
    def cdf(self, x: float) -> float:
        if x < self.a:
            return 0.0
        elif x > self.b:
            return 1.0
        else:
            return (x - self.a) / (self.b - self.a)

    # @vectorise_input    
    def inverse_cdf(self, p: float) -> float:
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be in the range [0, 1].")
        return self.a + p * (self.b - self.a)

    # Sampling

    def sample(self, size: int = 1) -> list[float]:
        """
        Generate n samples (n = size) from the Uniform distribution
        """
        # TODO: Implement sample method for uniform distribution manually
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        return np.random.uniform(low=self.a, high=self.b, size=size).tolist()
    