import numpy as np

from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions.abstract.continuous_distribution import ContinuousDistribution


class UniformDistribution(ContinuousDistribution):
    """
    Class for a Uniform distribution on the interval [a, b].
    """
    def __init__(self, a: float = 0.0, b: float = 1.0):
        if a >= b:
            raise ValueError("Lower bound 'a' must be less than upper bound 'b'.")
        self._a = a
        self._b = b

    # Special methods

    def __repr__(self) -> str:
        return f"UniformDistribution(a={self._a}, b={self._b})"
    
    def __str__(self) -> str:
        return f"U({self._a}, {self._b})"
    
    def __hash__(self) -> int:
        return hash((self._a, self._b))
    
    # Distribution parameters

    @property
    def a(self) -> float:
        return self._a
    
    @property
    def b(self) -> float:
        return self._b
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [self._a, self._b]

    # Moments
   
    @property
    def mean(self) -> float:
        return (self._a + self._b) / 2
    
    @property
    def variance(self) -> float:
        return (self._b - self._a) ** 2 / 12
    
    @property
    def skewness(self) -> float:
        return 0.0
    
    @property
    def kurtosis(self) -> float:
        return -1.2

    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if self._a <= x <= self._b:
            return 1 / (self._b - self._a)
        else:
            return 0.0

    # @vectorise_input    
    def cdf(self, x: float) -> float:
        if x < self._a:
            return 0.0
        elif x > self._b:
            return 1.0
        else:
            return (x - self._a) / (self._b - self._a)

    # @vectorise_input    
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        return self._a + p * (self._b - self._a)
    