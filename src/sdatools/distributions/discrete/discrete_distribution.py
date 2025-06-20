from abc import abstractmethod
from random import choices

from sdatools.distributions.distribution import Distribution


class DiscreteDistribution(Distribution):

    @abstractmethod
    def domain(self) -> list[float]:
        pass
    
    @abstractmethod
    def pmf(self, k: float) -> float:
        """Probability Mass Function"""
        pass

    @abstractmethod
    def cdf(self, k: float) -> float:
        """Cumulative Distribution Function"""
        pass

    def sample(self, size: int = 1) -> list[float]:
        """Generate a sample of size `size` from the discrete distribution."""
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        outcomes = self.domain()
        probabilities = [self.pmf(k) for k in outcomes]
        return choices(outcomes, weights=probabilities, k=size)
    