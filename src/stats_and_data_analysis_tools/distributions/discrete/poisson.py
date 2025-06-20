from math import comb, exp, sqrt, pi

from distributions.discrete.discrete_distribution import DiscreteDistribution


class PoissonDistribution(DiscreteDistribution):
    """A class representing a Poisson distribution with rate parameter lambda.
    
    Note: a PoissonDistribution(lam) object relates to the random variable X ~ Poisson(lam)."""
    
    def __init__(self, lam: float):
        if lam <= 0:
            raise ValueError("Rate parameter lambda must be positive.")
        self.lam = lam

    def __repr__(self) -> str:
        """String representation of the Poisson distribution."""
        return f"PoissonDistribution(lam={self.lam})"
    
    def __str__(self) -> str:
        """String representation of the Poisson distribution."""
        return f"Poisson({self.lam})"
    
    def __eq__(self, other: object) -> bool:
        """Check equality of two Poisson distributions."""
        if not isinstance(other, PoissonDistribution):
            return NotImplemented
        return self.lam == other.lam
    
    def __ne__(self, other: object) -> bool:
        """Check inequality of two Poisson distributions."""
        if not isinstance(other, PoissonDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        """Return a hash value for the Poisson distribution."""
        return hash(self.lam)
    
    def pmf(self, k: int) -> float:
        """Probability Mass Function for the Poisson distribution.
        
        P(X = k) = (lam^k * exp(-lam)) / k!
        """
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return (self.lam ** k * exp(-self.lam)) / comb(k, k)
    
    def cdf(self, k: int) -> float:
        """Cumulative Distribution Function for the Poisson distribution.
        
        P(X <= k) = sum(P(X = i) for i in range(0, k + 1))
        """
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return sum(self.pmf(i) for i in range(0, k + 1))
    
    def mean(self) -> float:
        return self.lam
    
    def variance(self) -> float:
        return self.lam
    
    def skewness(self) -> float:
        return 1 / sqrt(self.lam) if self.lam > 0 else float('inf')
    
    def kurtosis(self) -> float:
        return 1 / self.lam if self.lam > 0 else float('inf')
    