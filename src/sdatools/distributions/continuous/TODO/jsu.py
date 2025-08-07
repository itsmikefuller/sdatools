from math import exp, log, sqrt, pi, atan

from sdatools.distributions import ContinuousDistribution

# TODO: Check correctness of moments and properties of Johnson SU distribution
# Reference Wikipedia: https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution

class JohnsonSUDistribution(ContinuousDistribution):
    """A class representing a Johnson SU distribution with parameters gamma, delta, lambda, and xi.
    
    Note: a JohnsonSUDistribution(gamma, delta, lambda, xi) object relates to the random variable X ~ JSU(gamma, delta, lambda, xi)."""
    
    def __init__(self, gamma: float = 0.0, delta: float = 1.0, lam: float = 0.0, xi: float = 1.0):
        if delta <= 0:
            raise ValueError("Delta must be positive.")
        self.gamma = gamma
        self.delta = delta
        self.lam = lam
        self.xi = xi

    def __repr__(self) -> str:
        return f"JohnsonSUDistribution(gamma={self.gamma}, delta={self.delta}, lam={self.lam}, xi={self.xi})"
    
    def __str__(self) -> str:
        return f"JSU({self.gamma}, {self.delta}, {self.lam}, {self.xi})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, JohnsonSUDistribution):
            return NotImplemented
        return (self.gamma == other.gamma and self.delta == other.delta and
                self.lam == other.lam and self.xi == other.xi)
    
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, JohnsonSUDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.gamma, self.delta, self.lam, self.xi))
    
    def pdf(self, x: float) -> float:
        """Probability Density Function for the Johnson SU distribution.
        
        f(x) = (delta / (sqrt(2 * pi) * (x - lam))) * exp(-0.5 * ((gamma + delta * log((x - lam) / xi)) ** 2))
        for x > lam, 0 otherwise.
        """
        if x <= self.lam:
            return 0.0
        z = (self.gamma + self.delta * log((x - self.lam) / self.xi))
        return (self.delta / (sqrt(2 * pi) * (x - self.lam))) * exp(-0.5 * z ** 2)
    
    def cdf(self, x: float) -> float:
        """Cumulative Distribution Function for the Johnson SU distribution.
        
        F(x) = 0.5 + (1 / pi) * atan((gamma + delta * log((x - lam) / xi)) / sqrt(2))
        for x > lam, 0 otherwise.
        """
        if x <= self.lam:
            return 0.0
        z = (self.gamma + self.delta * log((x - self.lam) / self.xi))
        return 0.5 + (1 / pi) * atan(z / sqrt(2))
    
    def mean(self) -> float:
        """Mean of the Johnson SU distribution."""
        return self.lam + self.xi * exp(self.gamma + 0.5 * self.delta ** 2)
    
    def variance(self) -> float:
        """Variance of the Johnson SU distribution."""
        return (self.xi ** 2) * (exp(2 * self.gamma + self.delta ** 2) - exp(2 * self.gamma + self.delta ** 2 / 2))
    
    def skewness(self) -> float:
        """Skewness of the Johnson SU distribution."""
        return (exp(self.gamma + 0.5 * self.delta ** 2) * (exp(self.delta ** 2) - 1)) / \
               (sqrt(exp(2 * self.gamma + self.delta ** 2) - exp(2 * self.gamma + self.delta ** 2 / 2)) ** 3)
    
    def kurtosis(self) -> float:
        """Kurtosis of the Johnson SU distribution."""
        exp_delta_sq = exp(self.delta ** 2)
        return (exp_delta_sq * (exp_delta_sq - 1) * (exp_delta_sq + 2)) / \
               (exp(2 * self.gamma + self.delta ** 2) - exp(2 * self.gamma + self.delta ** 2 / 2)) ** 2
    