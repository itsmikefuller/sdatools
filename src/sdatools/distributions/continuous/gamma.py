from math import exp, sqrt, gamma
from scipy.special import gammainc

from sdatools.core.utils import vectorise_input, validate_probability
from sdatools.distributions import ContinuousDistribution


class GammaDistribution(ContinuousDistribution):
    """
    A class representing a Gamma distribution with parameters alpha and beta
    """

    def __init__(self, alpha: float = 1.0, beta: float = 1.0):  
        if alpha <= 0:
            raise ValueError("Shape parameter (alpha) must be positive.")
        self.alpha = alpha
        if beta <= 0:
            raise ValueError("Scale parameter (beta) must be positive.")
        self.beta = beta

    # Special methods

    def __repr__(self) -> str:
        return f"GammaDistribution(alpha={self.alpha}, beta={self.beta})"    

    def __str__(self) -> str:
        return f"Gamma({self.alpha}, {self.beta})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GammaDistribution):
            return NotImplemented
        return (self.alpha == other.alpha) and (self.beta == other.beta)   

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, GammaDistribution):
            return NotImplemented
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.alpha, self.beta))

    def __add__(self, other: 'GammaDistribution') -> 'GammaDistribution':
        """
        Add two Gamma distributions with the same shape parameter
        
        If X ~ Gamma(alpha_1, beta) and Y ~ Gamma(alpha_2, beta), then:

        X + Y ~ Gamma(alpha_1 + alpha_2, beta)
        """
        if not isinstance(other, GammaDistribution):
            raise TypeError("Can only add another GammaDistribution.")
        
        if self.beta != other.beta:
            raise ValueError("Can only add Gamma distributions with the same scale parameter (beta).")
        
        return GammaDistribution(self.alpha + other.alpha, self.beta)
    
    def __sub__(self, other: 'GammaDistribution') -> 'GammaDistribution':
        # TODO: Investigate if subtraction of Gamma distributions is defined
        raise NotImplementedError("Subtraction of Gamma distributions is not defined.")

    def __mul__(self, scalar) -> 'GammaDistribution':
        """
        Left multiplication to allow GammaDistribution * scalar
        
        If X ~ Gamma(alpha, beta) and c > 0, then c * X ~ Gamma(alpha, b / c)
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int or float).")
        
        if scalar <= 0:
            raise ValueError("Scalar must be positive for multiplication with GammaDistribution.")
        
        return GammaDistribution(self.alpha, self.beta / scalar)
    
    def __rmul__(self, other):
        """
        Right multiplication to allow scalar * GammaDistribution.
        """
        return self.__mul__(other)

    def __truediv__(self, scalar) -> 'GammaDistribution':
        """
        Divide the Gamma distribution by a scalar

        If X ~ Gamma(alpha, beta) and c > 0, then X / c ~ Gamma(alpha, b * c)
        """
        if not isinstance(scalar, (int, float)) or scalar == 0:
            raise ValueError("Can only divide by a non-zero scalar (int or float).")
        
        if scalar <= 0:
            raise ValueError("Scalar must be positive for division with GammaDistribution.")
        
        return GammaDistribution(self.alpha, self.beta * scalar)

    # Domain

    @property
    def domain(self) -> list[float]:
        return [0, float('inf')]
    
    # Moments
    
    @property
    def mean(self) -> float:
        return self.alpha * self.beta

    @property
    def variance(self) -> float:
        return self.alpha * self.beta ** 2
    
    @property
    def skewness(self) -> float:
        return 2.0 / sqrt(self.alpha)
    
    @property
    def kurtosis(self) -> float:
        return 6.0 / self.alpha
    
    # Distribution functions

    # @vectorise_input
    def pdf(self, x: float) -> float:
        if x < 0:
            return 0.0
        return (1.0 / (gamma(self.alpha) * self.beta ** self.alpha)) * (x ** (self.alpha - 1.0)) * exp(-(x / self.beta))
    
    # @vectorise_input
    def cdf(self, x: float) -> float:
        # TODO: Implement without SciPy 
        return gammainc(self.alpha, x / self.beta)
    
    # @vectorise_input
    def inverse_cdf(self, p: float) -> float:
        validate_probability(p)
        # TODO: Implement the inverse CDF for the Gamma distribution
        raise NotImplementedError("Inverse CDF for Gamma distribution is not implemented yet.")
    
    # Sampling
    
    def sample(self, size: int = 1) -> list[float]:
        # TODO: Implement sampling from the Gamma distribution
        raise NotImplementedError("Sampling from Gamma distribution is not implemented yet.")
