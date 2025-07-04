from abc import abstractmethod

from sdatools.distributions.base_distribution import Distribution


class ContinuousDistribution(Distribution):
    '''A base class for continuous probability distributions.'''

    @abstractmethod
    def pdf(self, x: float) -> float:
        """Probability Density Function"""
        pass

    @abstractmethod
    def cdf(self, x: float) -> float:
        """Cumulative Distribution Function"""
        pass

    def domain(self):
        raise NotImplementedError("Domain method is not implemented for this continuous distribution.")

    @abstractmethod
    def sample(self, size: int = 1) -> list[float]:
        """Generate a sample of size `size` from the continuous distribution."""
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        raise NotImplementedError("Sample method is not implemented for this continuous distribution.")
