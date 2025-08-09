from abc import abstractmethod

from sdatools.core.types import NumericLike, SeriesLike
from sdatools.distributions import Distribution


class ContinuousDistribution(Distribution):
    """
    Abstract base class for continuous probability distributions.

    Subclasses must implement the following methods / properties:
        - domain: Domain of the distribution.
        - mean: Mean of the distribution.
        - variance: Variance of the distribution.
        - skewness: Skewness of the distribution.
        - kurtosis: Excess kurtosis of the distribution.
        - sample(size=1): Generate n (n=size) samples from the distribution.
        - pdf(x): Probability density function.
        - cdf(x): Cumulative distribution function.
        - __repr__: String representation of the distribution.
        - __hash__: Hash representation of the distribution.

    Methods / properties provided:
        - stddev: Standard deviation of the distribution.
        - __str__: String representation (takes value of __repr__ if not provided).
        - __eq__, __ne__: Check if two distributions are equal / not equal.
    """
 
    # Distribution functions
    
    @abstractmethod
    def pdf(self, x: float) -> float:
        """
        Probability Density Function.
        """
        pass

    @abstractmethod
    def cdf(self, x: float) -> float:
        """
        Cumulative Distribution Function.
        """
        pass
