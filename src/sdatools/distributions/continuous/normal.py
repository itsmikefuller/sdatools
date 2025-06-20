from math import exp, sqrt, pi

from sdatools.functions.erf import erf
from sdatools.distributions.continuous.continuous_distribution import ContinuousDistribution


class NormalDistribution(ContinuousDistribution):
    """A class representing a normal distribution with mean mu and standard deviation sigma.
    
    Note: a NormalDistribution(mu, sigma) object relates to the random variable X ~ N(mu, sigma**2)."""
    
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):  
        self.mu = mu
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        self.sigma = sigma

    def __repr__(self) -> str:
        """String representation of the normal distribution."""
        return f"NormalDistribution(mu={self.mu}, sigma={self.sigma})"    

    def __str__(self) -> str:
        """String representation of the normal distribution."""
        return f"N({self.mu}, {self.sigma ** 2})"

    def __eq__(self, other: object) -> bool:
        """Check equality of two normal distributions."""
        if not isinstance(other, NormalDistribution):
            return NotImplemented
        return self.mu == other.mu and self.sigma == other.sigma    

    def __ne__(self, other: object) -> bool:
        """Check inequality of two normal distributions."""
        if not isinstance(other, NormalDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        """Return a hash value for the normal distribution."""
        return hash((self.mu, self.sigma))

    def __add__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """Add two normal distributions:
        if X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then
        X + Y ~ N(mu1 + mu2, sqrt(sigma1^2 + sigma2^2))"""
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only add another NormalDistribution.")
        new_mu = self.mu + other.mu
        new_sigma = sqrt(self.sigma ** 2 + other.sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)
    
    def __sub__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """Subtract two normal distributions:
        if X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then
        X - Y ~ N(mu1 - mu2, sqrt(sigma1^2 + sigma2^2))"""
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only subtract another NormalDistribution.")
        new_mu = self.mu - other.mu
        new_sigma = sqrt(self.sigma ** 2 + other.sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)

    def __mul__(self, scalar) -> 'NormalDistribution':
        """Left multiplication to allow NormalDistribution * scalar:
        if X ~ N(mu, sigma) and c in R, then
        c * X ~ N(c * mu, |c| * sigma)"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        new_mu = scalar * self.mu
        new_sigma = abs(scalar) * self.sigma
        return NormalDistribution(new_mu, new_sigma)
    
    def __rmul__(self, other):
        """Right multiplication to allow scalar * NormalDistribution."""
        return self.__mul__(other)

    def __truediv__(self, scalar) -> 'NormalDistribution':
        """Divide the normal distribution by a scalar:
        if X ~ N(mu, sigma), then
        X / c ~ N(mu / c, sigma / |c|) for c != 0"""
        if not isinstance(scalar, (int, float)) or scalar == 0:
            raise ValueError("Can only divide by a non-zero scalar (int or float).")
        new_mu = self.mu / scalar
        new_sigma = self.sigma / abs(scalar)
        return NormalDistribution(new_mu, new_sigma)

    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    
    def mean(self) -> float:
        return self.mu

    def variance(self) -> float:
        return self.sigma ** 2

    def pdf(self, x: float) -> float:
        """Calculate the probability density function of the normal distribution"""
        return (1 / (self.sigma * sqrt(2 * pi))) * exp(-((x - self.mu) ** 2) / (2 * self.sigma ** 2))
    
    def cdf(self, x: float) -> float:
        """Calculate the cumulative distribution function of the standard normal distribution:
        cdf(x) = \int_{-\infty}^{x} (1 / sqrt(2 * pi)) * exp(-t^2 / 2) dt"""
        # TODO: Implement using quadrature 
        return 0.5 * (1 + erf(x / sqrt(2)))
