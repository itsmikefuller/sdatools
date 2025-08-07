from math import exp

from sdatools.distributions import ContinuousDistribution


class ExponentialDistribution(ContinuousDistribution):
    """
    A class representing an Exponential distribution with rate parameter lambda
    """
    
    def __init__(self, lam: float = 1.0):
        if lam <= 0:
            raise ValueError("Rate parameter lambda must be positive.")
        self.lam = lam

    # Special methods

    def __repr__(self) -> str:
        return f"ExponentialDistribution(lam={self.lam})"
    
    def __str__(self) -> str:
        return f"Exp({self.lam})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExponentialDistribution):
            return NotImplemented
        return self.lam == other.lam
    
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, ExponentialDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash(self.lam)
    
    # Domain

    def domain(self) -> list[float]:
        return [0, float('inf')]

    # Moments
    
    def mean(self) -> float:
        return 1.0 / self.lam
    
    def variance(self) -> float:
        return 1.0 / (self.lam ** 2)
    
    def skewness(self) -> float:
        return 2.0
    
    def kurtosis(self) -> float:
        return 6.0
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return self.lam * exp(-self.lam * x)
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return 1.0 - exp(-self.lam * x)
    