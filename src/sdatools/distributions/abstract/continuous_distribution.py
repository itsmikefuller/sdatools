from abc import abstractmethod

from sdatools.core.types import NumericLike, SeriesLike
from sdatools.distributions import Distribution


class ContinuousDistribution(Distribution):
    """
    Abstract base class for continuous probability distributions.

    Subclasses must implement:
    --------------------------
    - domain          : Domain of the distribution.
    - mean            : Mean of the distribution.
    - variance        : Variance of the distribution.
    - skewness        : Skewness of the distribution.
    - kurtosis        : Excess kurtosis of the distribution.
    - pdf(x)          : Probability density function.
    - cdf(x)          : Cumulative distribution function.
    - sample(size=1)  : Generate n (n=size) samples from the distribution.
    - __repr__        : String representation of the distribution.
    - __hash__        : Hash representation of the distribution.

    Provided by base class:
    -----------------------
    - stddev          : Standard deviation of the distribution.
    - __str__         : Shortened string representation (defaults to __repr__).
    - __eq__          : Check if two distributions are equal
    - __ne__          : Check if two distributions are not equal.
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
