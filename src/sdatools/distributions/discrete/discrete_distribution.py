from abc import abstractmethod
from random import choices

from sdatools.distributions.distribution import Distribution


class DiscreteDistribution(Distribution):

    @abstractmethod
    def domain(self) -> list[float]:
        pass
    
    @abstractmethod
    def pmf(self, k) -> float:
        """Probability Mass Function"""
        pass

    @abstractmethod
    def cdf(self, k) -> float:
        """Cumulative Distribution Function"""
        pass

    # TODO: Determine a better way to sample for discrete distributions.
    # The current implementation uses the domain and PMF to generate samples.
    # For e.g. Poisson, where terms in the PMF are very large/small, we get an overflow error.
    def sample(self, size: int = 1) -> list[float]:
        """Generate a sample of size `size` from the discrete distribution."""
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        if not isinstance(size, int):
            raise ValueError("Sample size must be an integer.")
        outcomes = self.domain()
        probabilities = [self.pmf(k) for k in outcomes]
        return choices(outcomes, weights=probabilities, k=size)
    