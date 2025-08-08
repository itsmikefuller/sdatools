from math import log, exp, sqrt

from sdatools.distributions import DiscreteDistribution


class PoissonDistribution(DiscreteDistribution):
    """
    A class representing a Poisson distribution with rate parameter lambda
    """
    
    def __init__(self, lam: float):
        if lam <= 0:
            raise ValueError("Rate parameter lambda must be positive.")
        self._lam = lam
    
    # Special methods

    def __repr__(self) -> str:
        return f"PoissonDistribution(lam={self._lam})"
    
    def __str__(self) -> str:
        return f"Poisson({self._lam})"
    
    def __hash__(self) -> int:
        return hash(self._lam)
    
    # Distribution parameters

    @property
    def lam(self) -> float:
        return self._lam
    
    # Domain
    
    @property
    def domain(self) -> list[float]:
        # Find maximum integer that produces PMF above machine epsilon
        k = 0
        while self.pmf(k) > 1e-10:
            k += 1
        return list(range(0, k + 1))
    
    # Moments
    
    @property
    def mean(self) -> float:
        return self._lam
    
    @property
    def variance(self) -> float:
        return self._lam
    
    @property
    def skewness(self) -> float:
        return 1 / sqrt(self._lam) if self._lam > 0 else float('inf')
    
    @property
    def kurtosis(self) -> float:
        return 1 / self._lam if self._lam > 0 else float('inf')
    
    # Distribution functions

    def pmf(self, k: int) -> float:
        """
        P(X = k) = (lam^k * exp(-lam)) / k!
        """
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        
        log_pmf = self._lam * k - self._lam - sum(log(i) for i in range(1, k + 1)) if k > 0 else -self._lam
        return exp(log_pmf)
    
    def cdf(self, k: int) -> float:
        """
        P(X <= k) = sum(P(X = i) for i in range(0, k + 1))
        """
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return sum(self.pmf(i) for i in range(0, k + 1))
 