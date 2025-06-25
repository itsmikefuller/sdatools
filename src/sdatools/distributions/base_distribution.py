from abc import ABC, abstractmethod

from math import sqrt


class Distribution(ABC):
    '''A base class for probability distributions.'''

    @abstractmethod
    def mean(self) -> float:
        pass

    @abstractmethod
    def variance(self) -> float:
        pass

    def stddev(self) -> float:
        return sqrt(self.variance())

    @abstractmethod
    def skewness(self) -> float:
        pass

    @abstractmethod
    def kurtosis(self) -> float:
        pass

    @abstractmethod
    def domain(self) -> list[float]:
        pass

    @abstractmethod
    def sample(self, size: int = 1) -> list[float]:
        pass

    def sample_mean_distribution(self, n):
        pass
        # TODO: Implement sample mean distribution
        # return SampleMeanDistribution(self, n)

    def sample_variance_distribution(self, n):
        pass
        # TODO: Implement sample variance distribution
        # return SampleVarianceDistribution(self, n)
