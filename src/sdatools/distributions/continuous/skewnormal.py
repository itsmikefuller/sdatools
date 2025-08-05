from math import exp, sqrt, pi
import numpy as np
from scipy.stats import skewnorm

from sdatools.core.functions.erf import erf
from sdatools.distributions.continuous.continuous_distribution import ContinuousDistribution


class SkewNormalDistribution(ContinuousDistribution):
    """
    A class representing a skew-normal distribution with location xi, scale omega, and shape alpha
    """
    
    def __init__(self, xi: float = 0.0, omega: float = 1.0, alpha: float = 0.0):  
        self.xi = xi
        if omega <= 0:
            raise ValueError("Scale parameter omega must be positive.")
        self.omega = omega
        self.alpha = alpha
        self._delta = alpha / sqrt(1 + alpha ** 2)

    # Special methods

    def __repr__(self) -> str:
        return f"SkewNormalDistribution(xi={self.xi}, omega={self.omega}, alpha={self.alpha})"    

    def __str__(self) -> str:
        return f"SN({self.xi}, {self.omega}, {self.alpha})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SkewNormalDistribution):
            return NotImplemented
        return (self.xi == other.xi) and (self.omega == other.omega) and (self.alpha == other.alpha)   

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, SkewNormalDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.xi, self.omega, self.alpha))
    
    # Domain

    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    
    # Moments
    
    def mean(self) -> float:
        return self.xi + (self.omega * sqrt(2 / pi) * self._delta)

    def variance(self) -> float:
        return (self.omega ** 2) * (1 - (2 * self._delta ** 2) / pi)
    
    def skewness(self) -> float:
        return (4 - pi) / 2 * (self._delta * sqrt(2 / pi)) ** 3 / ((1 - 2 * self._delta ** 2 / pi) ** (3/2))
    
    def kurtosis(self) -> float:
        return 2 * (pi - 3) * (self._delta * sqrt(2 / pi)) ** 4 / ((1 - 2 * self._delta ** 2 / pi) ** 2)
    
    # Distribution functions

    def pdf(self, x: float) -> float:
        # TODO: Implement Normal PDF (phi(x)) and CDF (Phi(x)) functions in core, use them in NormalDistribution and here
        z = (x - self.xi) / self.omega
        phi = (1 / sqrt(2 * pi)) * exp(-0.5 * z ** 2)
        Phi = 0.5 * (1 + erf(self.alpha * z / sqrt(2)))
        return 2 * phi * Phi / self.omega
    
    def cdf(self, x: float) -> float:
        # TODO: Implement without scipy
        return float(skewnorm.cdf(x, self.alpha, loc=self.xi, scale=self.omega))
    
    def inverse_cdf(self, p: float) -> float:
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be in the range [0, 1].")
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
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        raise NotImplementedError("Sampling from SkewNormalDistribution is not implemented yet.")
        # return skewnorm.rvs(self.alpha, loc=self.xi, scale=self.omega, size=size).tolist()
    