from math import comb, exp, sqrt, pi

from sdatools.distributions import DiscreteDistribution


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

    # Special methods

    def __repr__(self) -> str:
        return f"BinomialDistribution(n={self.n}, p={self.p})"
    
    def __str__(self) -> str:
        return f"Bin({self.n}, {self.p})"
    
    def __hash__(self) -> int:
        return hash((self.n, self.p))
    
    # Domain

    @property
    def domain(self) -> list[int]:
        return list(range(0, self.n + 1))
    
    # Moments
    
    @property
    def mean(self) -> float:
        return self.n * self.p
    
    @property
    def variance(self) -> float:
        return self.n * self.p * (1 - self.p)
    
    @property
    def mode(self) -> int:
        return int((self.n + 1) * self.p)
    
    @property
    def skewness(self) -> float:
        if self.n == 0 or self.p in (0, 1):
            return 0.0
        return (1 - 2 * self.p) / sqrt(self.n * self.p * (1 - self.p))
    
    @property
    def kurtosis(self) -> float:
        if self.n == 0 or self.p in (0, 1):
            return 0.0
        return (1 - 6 * self.p * (1 - self.p)) / (self.n * self.p * (1 - self.p))
    
    # Distribution functions

    def pmf(self, k: int) -> float:
        """
        P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)

        where C(n, k) is the binomial coefficient, "n choose k"
        """
        if k < 0 or k > self.n:
            return 0.0
        if not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
    
    def cdf(self, k: int) -> float:
        """
        P(X <= k) = sum(P(X = i) for i in range(0, k + 1))
        """
        if k < 0:
            return 0.0
        if not isinstance(k, int):
            raise ValueError("k must be a non-negative integer.")
        return sum(self.pmf(i) for i in range(0, k + 1))   
    