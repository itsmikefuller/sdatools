from abc import ABC, abstractmethod
from math import sqrt

from sdatools.core.types import SeriesLike


class Distribution(ABC):
    """
    Abstract base class for probability distributions.

    Subclasses must implement the following methods / properties:
        - domain: Domain of the distribution.
        - mean: Mean of the distribution.
        - variance: Variance of the distribution.
        - skewness: Skewness of the distribution.
        - kurtosis: Excess kurtosis of the distribution.
        - sample(size=1): Generate n (n=size) samples from the distribution.
        - __repr__: String representation of the distribution.
        - __hash__: Hash representation of the distribution.

    Methods / properties provided:
        - stddev: Standard deviation of the distribution.
        - __str__: String representation (takes value of __repr__ if not overridden).
        - __eq__: Check if two distributions are equal
        - __ne__: Check if two distributions are not equal.
    """

    # Special methods

    def __eq__(self, other: object) -> bool:
        """
        Check if two distributions are equal.
        
        If two distributions are equal, all their parameters should be identical.
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other: object) -> bool:
        """
        Check if two distributions are not equal.
        """
        eq_check = self.__eq__(other)
        return NotImplemented if eq_check is NotImplemented else not eq_check
    
    @abstractmethod
    def __hash__(self) -> int:
        """
        Hash representation of the distribution.

        Should include all parameters of the distribution.
        """
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        """
        String representation of the distribution.

        For example: Distribution(param1=x1, param2=x2, ...).

        String representation should include all parameters of the distribution.
        """
        pass

    def __str__(self) -> str:
        """
        Shortened string representation for the distribution.

        For example: Bin(n, p).

        If not overridden, __repr__ is used.
        """
        return self.__repr__()
    

    # Domain
    
    # TODO: Determine a better way to represent a distribution domain
    @property
    @abstractmethod
    def domain(self) -> list[int] | list[float]:
        """
        Domain of the distribution.

        For continuous distributions, this is typically an interval [a, b] or (-inf, inf).

        For discrete distributions, this is typically a set of points.
        """
        pass # TODO: How to represent open intervals in Python? Use a list or tuple?
    

    # Moments
    
    @property
    @abstractmethod
    def mean(self) -> float:
        """
        Mean of the distribution.

        For continuous distributions, this is defined as:
        mean = E[X] = ∫ x * f(x) dx,
        where f(x) is the probability density function of the distribution.
        
        For discrete distributions, this is defined as:
        mean = Σ x * P(X = x),
        where P(X = x) is the probability mass function.
        """
        pass

    @property
    @abstractmethod
    def variance(self) -> float:
        """
        Variance of the distribution.

        variance = E[(X - mu) ** 2] = E[X ** 2] - mu ** 2,
        where mu is the mean of the distribution.
        """
        pass

    @property
    def stddev(self) -> float:
        """
        Standard deviation of the distribution.

        stddev = sqrt(variance).
        """
        return sqrt(self.variance)

    @property
    @abstractmethod
    def skewness(self) -> float:
        """
        Skewness of the distribution.

        skewness = E[(X - mu) ** 3] / sigma ** 3,
        where mu is the mean and sigma is the standard deviation.
        """
        pass

    @property
    @abstractmethod
    def kurtosis(self) -> float:
        """
        Excess kurtosis of the distribution.

        kurtosis = E[(X - mu) ** 4] / sigma ** 4 - 3,
        where mu is the mean and sigma is the standard deviation.
        """
        pass

    
    # Sampling

    # TODO: Make sample() an enforced method and implement in all distributions
    # @abstractmethod
    def sample(self, size: int = 1) -> SeriesLike:
        """
        Generate n (n=size) samples from the distribution.
        """
        raise NotImplementedError("Sampling from a distribution not yet implemented.")
    
    # TODO: Implement sample mean distribution
    def sample_mean_distribution(self, n):
        pass
    
    # TODO: Implement sample variance distribution
    def sample_variance_distribution(self, n):
        pass
