from math import sqrt, exp, sinh, cosh
import numpy as np
from scipy.stats import norm

from sdatools.core.functions import phi, Phi
from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class JohnsonSUDistribution(ContinuousDistribution):
    """
    A class representing the Johnson's SU distribution family
    """
    
    def __init__(self, gamma: float = 1.0, delta: float = 2.0, xi: float = 1.0, lam: float = 1.0):  
        if gamma <= 0:
            raise ValueError(f"Parameter gamma must be positive.")
        if delta <= 0:
            raise ValueError(f"Parameter delta must be positive.")
        if xi <= 0:
            raise ValueError(f"Parameter xi must be positive.")
        if lam <= 0:
            raise ValueError(f"Parameter lam must be positive.")
        self._gamma = gamma
        self._delta = delta
        self._xi = xi
        self._lam = lam

        self._deltaminus2 = self._delta ** (-2)

    # Special methods

    def __repr__(self) -> str:
        return f"JohnsonSUDistribution(gamma={self._gamma}, delta={self._delta}, xi={self._xi}, lam={self._lam})"    

    def __str__(self) -> str:
        return f"JSU({self._gamma}, {self._delta}, {self._xi}, {self._lam})"
    
    def __hash__(self) -> int:
        return hash((self._gamma, self._delta, self._xi, self._lam))
    
    # Distribution parameters

    @property
    def gamma(self) -> float:
        return self._gamma
    
    @property
    def delta(self) -> float:
        return self._delta
    
    @property
    def xi(self) -> float:
        return self._xi
    
    @property
    def lam(self) -> float:
        return self._lam

    # Domain

    @property
    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    
    # Moments
    
    @property
    def mean(self) -> float:
        trm1: float = self._lam * exp(self._deltaminus2 / 2)
        trm2: float = sinh(self._gamma / self._delta)
        return self._xi - trm1 * trm2

    @property
    def variance(self) -> float:
        trm1: float = self._lam ** 2 / 2
        trm2: float = (exp(self._deltaminus2) - 1)
        trm3: float = (exp(self._deltaminus2) * cosh(2 * self._gamma / self._delta) + 1)
        return trm1 * trm2 * trm3
    
    @property
    def skewness(self) -> float:
        num1: float = self._lam ** 3 * sqrt(exp(self._deltaminus2))
        num2: float = (exp(self._deltaminus2) - 1) ** 2
        num3: float = (exp(self._deltaminus2) * (exp(self._deltaminus2) + 2) * sinh(3 * self._gamma / self._delta) + 3 * sinh(self._gamma / self._delta))
        denom: float = 4 * self.variance ** 1.5
        return - num1 * num2 * num3 / denom
    
    @property
    def kurtosis(self) -> float:
        k1: float = (exp(self._deltaminus2)) ** 2 * ((exp(self._deltaminus2)) ** 4 + 2 * (exp(self._deltaminus2)) ** 3 + 3 * (exp(self._deltaminus2)) ** 2 - 3) * cosh(4 * self._gamma / self._delta)
        k2: float = 4 * (exp(self._deltaminus2)) ** 2 * (exp(self._deltaminus2) + 2) * cosh(3 * self._gamma / self._delta)
        k3: float = 3 * (2 * exp(self._deltaminus2) + 1)
        num: float = self._lam ** 4 * (exp(self._deltaminus2) - 1) ** 2 * (k1 + k2 + k3)
        denom: float = 8 * self.variance ** 2
        return num / denom
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        z: float = (x - self._xi) / self._lam
        trm1: float = self._delta / self._lam
        trm2: float = 1.0 / sqrt(1 + z ** 2)
        trm3: float = phi(self._gamma + self._delta * np.arcsinh(z))
        return trm1 * trm2 * trm3
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        z: float = (x - self._xi) / self._lam
        return Phi(self._gamma + self._delta * np.arcsinh(z))
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement inverse CDF of Johnson SU distribution
        raise NotImplementedError("Inverse CDF not implemented for Johnson's SU distribution")
    
    # Sampling
    
    # TODO: Implement sampling from a Johnson SU distribution
    def sample(self, size: int = 1) -> list[float]:
        """
        Generate n samples (n = size) from the Johnson's SU distribution
        """
        # TODO: Implement manually using Box-Muller transform or similar method
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        raise NotImplementedError("Sampling from Johnson SU distribution not yet implemented")
    