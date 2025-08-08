from abc import ABC, abstractmethod

from math import sqrt


class Distribution(ABC):
    """
    A base class for all probability distributions
    """

    # Special methods

    def __eq__(self, other: object) -> bool:
        """
        Check if two distributions are equal
        
        If two distributions are equal, all their parameters should be identical
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other: object) -> bool:
        """
        Check if two distributions are not equal
        """
        eq_check = self.__eq__(other)
        return NotImplemented if eq_check is NotImplemented else not eq_check
    
    @abstractmethod
    def __hash__(self) -> int:
        """
        Hash representation of the distribution

        Should include all parameters of the distribution
        """
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        """
        String representation for the distribution, in the form:

        Distribution(param1=x1, param2=x2, ...)

        Should include all parameters of the distribution
        """
        pass

    def __str__(self) -> str:
        """
        Shortened string representation for the distribution

        If not overridden to something more appropriate (e.g. Bin(n, p)), __repr__ is used
        """
        return self.__repr__()
    
    # Domain
    
    # TODO: Determine a better way to represent a distribution domain
    @property
    @abstractmethod
    def domain(self) -> list[int] | list[float]:
        """
        Returns the domain of the distribution

        For continuous distributions, this is typically an interval [a, b] or (-inf, inf)

        For discrete distributions, this is typically a set of points
        """
        pass # TODO: How to represent open intervals in Python? Use a list or tuple?
    
    # Moments
    
    @property
    @abstractmethod
    def mean(self) -> float:
        """
        Returns the mean of the distribution

        For continuous distributions, this is defined as:
        mean = E[X] = ∫ x * f(x) dx
        where f(x) is the probability density function of the distribution
        
        For discrete distributions, this is defined as:
        mean = Σ x * P(X = x)
        where P(X = x) is the probability mass function
        """
        pass

    @property
    @abstractmethod
    def variance(self) -> float:
        """
        Returns the variance of the distribution, defined as:
        variance = E[(X - mu) ** 2] = E[X ** 2] - mu ** 2
        where mu is the mean of the distribution
        """
        pass

    @property
    def stddev(self) -> float:
        """
        Returns the standard deviation of the distribution, defined as:
        stddev = sqrt(variance)
        """
        return sqrt(self.variance)

    @property
    @abstractmethod
    def skewness(self) -> float:
        """
        Returns the skewness of the distribution, defined as:
        skewness = E[(X - mu) ** 3] / sigma ** 3
        where mu is the mean and sigma is the standard deviation
        """
        pass

    @property
    @abstractmethod
    def kurtosis(self) -> float:
        """
        Returns the excess kurtosis, which is defined as:
        kurtosis = E[(X - mu) ** 4] / sigma ** 4 - 3
        where mu is the mean and sigma is the standard deviation
        """
        pass

    # Sampling

    # TODO: Make sample() an enforced method and implement in all distributions
    # @abstractmethod
    def sample(self, size: int = 1) -> list[float]:
        """
        Return a list of n (n=size) samples from the distribution
        """
        raise NotImplementedError("Sampling from a distribution not yet implemented.")
    
    # TODO: Implement sample mean distribution
    def sample_mean_distribution(self, n):
        pass
    
    # TODO: Implement sample variance distribution
    def sample_variance_distribution(self, n):
        pass
