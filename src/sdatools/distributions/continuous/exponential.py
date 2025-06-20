from math import exp, sqrt, pi

from sdatools.distributions.continuous.continuous_distribution import ContinuousDistribution


class ExponentialDistribution(ContinuousDistribution):
    """A class representing an exponential distribution with rate parameter lambda.
    
    Note: an ExponentialDistribution(lam) object relates to the random variable X ~ Exp(lam)."""
    
    def __init__(self, lam: float):
        if lam <= 0:
            raise ValueError("Rate parameter lambda must be positive.")
        self.lam = lam

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
    
    def pdf(self, x: float) -> float:
        """Probability Density Function for the exponential distribution.
        
        f(x) = lam * exp(-lam * x) for x >= 0, 0 otherwise.
        """
        if x < 0:
            return 0.0
        return self.lam * exp(-self.lam * x)
    
    def cdf(self, x: float) -> float:
        """Cumulative Distribution Function for the exponential distribution.
        
        F(x) = 1 - exp(-lam * x) for x >= 0, 0 otherwise.
        """
        if x < 0:
            return 0.0
        return 1 - exp(-self.lam * x)
    
    def mean(self) -> float:
        return 1 / self.lam
    
    def variance(self) -> float:
        return 1 / (self.lam ** 2)
    
    def skewness(self) -> float:
        return 2.0
    
    def kurtosis(self) -> float:
        return 6.0
