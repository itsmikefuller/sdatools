from math import exp

from sdatools.distributions import ContinuousDistribution


class ExponentialDistribution(ContinuousDistribution):
    """
    A class representing an Exponential distribution with rate parameter lambda
    """
    
    def __init__(self, lam: float = 1.0):
        if lam <= 0:
            raise ValueError("Rate parameter lambda must be positive.")
        self._lam = lam

    # Parameters

    @property
    def lam(self) -> float:
        return self._lam

    # Special methods

    def __repr__(self) -> str:
        return f"ExponentialDistribution(lam={self._lam})"
    
    def __str__(self) -> str:
        return f"Exp({self._lam})"
    
    def __hash__(self) -> int:
        return hash(self._lam)
    
    # Domain

    @property
    def domain(self) -> list[float]:
        return [0, float('inf')]

    # Moments
    
    @property
    def mean(self) -> float:
        return 1.0 / self._lam
    
    @property
    def variance(self) -> float:
        return 1.0 / (self._lam ** 2)
    
    @property
    def skewness(self) -> float:
        return 2.0
    
    @property
    def kurtosis(self) -> float:
        return 6.0
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return self._lam * exp(-self._lam * x)
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return 1.0 - exp(-self._lam * x)
    