from math import comb, exp, sqrt, pi

from sdatools.distributions.discrete.discrete_distribution import DiscreteDistribution


class BinomialDistribution(DiscreteDistribution):
    """A class representing a binomial distribution with number of trials n and probability of success p.
    
    Note: a BinomialDistribution(n, p) object relates to the random variable X ~ B(n, p)."""
    
    def __init__(self, n: int, p: float):
        if n < 0:
            raise ValueError("Number of trials must be non-negative.")
        if not (0 <= p <= 1):
            raise ValueError("Probability of success must be between 0 and 1.")
        self.n = n
        self.p = p

    def __repr__(self) -> str:
        """String representation of the binomial distribution."""
        return f"BinomialDistribution(n={self.n}, p={self.p})"
    
    def __str__(self) -> str:
        """String representation of the binomial distribution."""
        return f"B({self.n}, {self.p})"

    def __eq__(self, other: object) -> bool:
        """Check equality of two binomial distributions."""
        if not isinstance(other, BinomialDistribution):
            return NotImplemented
        return self.n == other.n and self.p == other.p
    
    def __ne__(self, other: object) -> bool:
        """Check inequality of two binomial distributions."""
        if not isinstance(other, BinomialDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        """Return a hash value for the binomial distribution."""
        return hash((self.n, self.p))
    
    def pmf(self, k: int) -> float:
        """Probability Mass Function for the binomial distribution.
        
        P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
        where C(n, k) is the binomial coefficient "n choose k".
        """
        if k < 0 or k > self.n:
            return 0.0
        if not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
    
    def cdf(self, k: int) -> float:
        """Cumulative Distribution Function for the binomial distribution.
        
        P(X <= k) = sum(P(X = i) for i in range(0, k + 1))
        """
        if k < 0:
            return 0.0
        if not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return sum(self.pmf(i) for i in range(0, k + 1))

    def mean(self) -> float:
        """Mean of the binomial distribution."""
        return self.n * self.p
    
    def variance(self) -> float:
        """Variance of the binomial distribution."""
        return self.n * self.p * (1 - self.p)
    
    def mode(self) -> int:
        """Mode of the binomial distribution.
        
        The mode is given by floor((n + 1) * p).
        If n * p is an integer, both floor and ceil give the same mode.
        """
        return int((self.n + 1) * self.p)
    
    def skewness(self) -> float:
        """Skewness of the binomial distribution.
        
        Skewness = (1 - 2 * p) / sqrt(n * p * (1 - p))
        """
        if self.n == 0 or self.p in (0, 1):
            return 0.0
        return (1 - 2 * self.p) / sqrt(self.n * self.p * (1 - self.p))
    
    def kurtosis(self) -> float:
        """Kurtosis of the binomial distribution.
        
        Kurtosis = (1 - 6 * p * (1 - p)) / (n * p * (1 - p))
        """
        if self.n == 0 or self.p in (0, 1):
            return 0.0
        return (1 - 6 * self.p * (1 - self.p)) / (self.n * self.p * (1 - self.p))
    
    def sample(self, size: int = 1) -> list[int]:
        """Generate a sample of size `size` from the binomial distribution."""
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        
        from random import choices
        return choices(range(self.n + 1), weights=[self.pmf(k) for k in range(self.n + 1)], k=size)
