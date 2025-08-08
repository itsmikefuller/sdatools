from abc import ABC, abstractmethod

from math import sqrt


class Distribution(ABC):
    """
    A base class for all probability distributions
    """

    # TODO: Implement common special methods here, instead of in each distribution

    # def __eq__(self, other: object) -> bool:
    #     if not isinstance(other, Distribution):
    #         return NotImplemented
    #     return self.n == other.n and self.p == other.p
    
    # def __ne__(self, other: object) -> bool:
    #     if not isinstance(other, Distribution):
    #         return NotImplemented
    #     return not self.__eq__(other)
    
    # def __hash__(self) -> int:
    #     return hash((self.n, self.p))
    
    
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
