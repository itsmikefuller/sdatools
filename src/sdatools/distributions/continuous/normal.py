from math import sqrt
from scipy.stats import norm

from sdatools.core.functions import phi, Phi
from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class NormalDistribution(ContinuousDistribution):
    """
    Class for a Normal distribution with mean mu and standard deviation sigma
    
    Note: a NormalDistribution(mu, sigma) object relates to the random variable X ~ N(mu, sigma**2)
    """
    
    def __init__(self, mu: float = 0.0, sigma: float = 1.0):  
        if sigma <= 0:
            raise ValueError("Standard deviation must be positive.")
        self._mu = mu
        self._sigma = sigma

    # Special methods

    def __repr__(self) -> str:
        return f"NormalDistribution(mu={self._mu}, sigma={self._sigma})"    

    def __str__(self) -> str:
        return f"N({self._mu}, {self._sigma ** 2})"
    
    def __hash__(self) -> int:
        return hash((self._mu, self._sigma))

    def __add__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """
        Add two normal distributions

        If X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then X + Y ~ N(mu1 + mu2, sqrt(sigma1^2 + sigma2^2))
        """
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only add another NormalDistribution.")
        new_mu = self._mu + other._mu
        new_sigma = sqrt(self._sigma ** 2 + other._sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)
    
    def __sub__(self, other: 'NormalDistribution') -> 'NormalDistribution':
        """
        Subtract two normal distributions

        If X ~ N(mu1, sigma1) and Y ~ N(mu2, sigma2), then X - Y ~ N(mu1 - mu2, sqrt(sigma1^2 + sigma2^2))
        """
        if not isinstance(other, NormalDistribution):
            raise TypeError("Can only subtract another NormalDistribution.")
        new_mu = self._mu - other._mu
        new_sigma = sqrt(self._sigma ** 2 + other._sigma ** 2)
        return NormalDistribution(new_mu, new_sigma)

    def __mul__(self, scalar) -> 'NormalDistribution':
        """
        Left multiplication to allow NormalDistribution * scalar

        If X ~ N(mu, sigma) and c in R, then c * X ~ N(c * mu, |c| * sigma)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        new_mu = scalar * self._mu
        new_sigma = abs(scalar) * self._sigma
        return NormalDistribution(new_mu, new_sigma)
    
    def __rmul__(self, other):
        """
        Right multiplication to allow scalar * NormalDistribution
        """
        return self.__mul__(other)

    def __truediv__(self, scalar) -> 'NormalDistribution':
        """
        Divide the normal distribution by a scalar

        If X ~ N(mu, sigma) and c != 0, then X / c ~ N(mu / c, sigma / |c|)
        """
        if not isinstance(scalar, (int, float)) or scalar == 0:
            raise ValueError("Can only divide by a non-zero scalar (int or float).")
        new_mu = self._mu / scalar
        new_sigma = self._sigma / abs(scalar)
        return NormalDistribution(new_mu, new_sigma)
    

    # Distribution parameters

    @property
    def mu(self) -> float:
        return self._mu
    
    @property
    def sigma(self) -> float:
        return self._sigma
    

    # Domain

    @property
    def domain(self) -> list[float]:
        return [float('-inf'), float('inf')]
    

    # Moments
    
    @property
    def mean(self) -> float:
        return self._mu

    @property
    def variance(self) -> float:
        return self._sigma ** 2
    
    @property
    def skewness(self) -> float:
        return 0.0
    
    @property
    def kurtosis(self) -> float:
        return 0.0
    

    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        return phi((x - self._mu) / self._sigma) / self._sigma
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        return Phi((x - self._mu) / self._sigma)
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement without using SciPy for better understanding
        return float(norm.ppf(p, loc=self._mu, scale=self._sigma))
    
   