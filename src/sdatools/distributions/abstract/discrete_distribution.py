from abc import abstractmethod
from random import choices

from sdatools.distributions import Distribution


class DiscreteDistribution(Distribution):
    """
    Abstract base class for discrete probability distributions.
        
    Subclasses must implement:
    --------------------------
    - domain          : Domain of the distribution.
    - mean            : Mean of the distribution.
    - variance        : Variance of the distribution.
    - skewness        : Skewness of the distribution.
    - kurtosis        : Excess kurtosis of the distribution.
    - pmf(x)          : Probability mass function.
    - cdf(x)          : Cumulative distribution function.
    - __repr__        : String representation of the distribution.
    - __hash__        : Hash representation of the distribution.

    Provided by base class:
    -----------------------
    - stddev          : Standard deviation of the distribution.
    - sample(size=1)  : Generate n (n=size) samples from the distribution.
    - __str__         : Shortened string representation (defaults to __repr__).
    - __eq__          : Check if two distributions are equal
    - __ne__          : Check if two distributions are not equal.
    """

    # Distribution functions
    
    @abstractmethod
    def pmf(self, k) -> float:
        """
        Probability mass function.
        """
        pass

    @abstractmethod
    def cdf(self, k) -> float:
        """
        Cumulative distribution function.
        """
        pass

    # Sampling

    # TODO: Determine a better way to sample for discrete distributions.
    # The current implementation uses the domain and PMF to generate samples.
    # For e.g. Poisson, where terms in the PMF are very large/small, we get an overflow error.
    def sample(self, size: int = 1) -> list[float]:
        """
        Generate a list of n (n=size) samples from the discrete distribution
        """
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        outcomes = self.domain
        probabilities = [self.pmf(k) for k in outcomes]
        return choices(outcomes, weights=probabilities, k=size)
    