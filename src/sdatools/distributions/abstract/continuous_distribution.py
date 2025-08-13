from abc import abstractmethod
import numpy as np

from sdatools.core.types import ArrayLike, SeriesLike
from sdatools.distributions.abstract.distribution import Distribution


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

    Optional further implementations:
    ---------------------------------
    - inverse_cdf()   : Inverse cumulative distribution function.

    Provided by base class:
    -----------------------
    - stddev          : Standard deviation of the distribution.
    - __str__         : Shortened string representation (defaults to __repr__).
    - __eq__          : Check if two distributions are equal
    - __ne__          : Check if two distributions are not equal.

    Notes:
    ------
    - If inverse_cdf() is implemented, then sample() is auto-implemented using the inverse CDF.
    """
 
    # Distribution functions
    
    @abstractmethod
    def pdf(self, x: float) -> float:
        """
        Probability density function.
        """
        pass

    @abstractmethod
    def cdf(self, x: float) -> float:
        """
        Cumulative distribution function.
        """
        pass

    def inverse_cdf(self, p: float) -> float:
        """
        Inverse cumulative distribution function.
        """
        raise NotImplementedError(f"{self.__class__.__name__} does not implement inverse_cdf().")


    # Sampling

    def sample(self, size: int = 1) -> SeriesLike:
        """
        Generate n (n=size) samples from the distribution.

        If inverse_cdf() has been implemented, samples will be generated using the inverse CDF.
        """
        if size <= 0:
            raise ValueError("Sample size must be a positive integer.")
        try:
            u: np.ndarray = np.random.random(size)
            return np.array([self.inverse_cdf(ui) for ui in u])
        except NotImplementedError:
            raise NotImplementedError(f"{self.__class__.__name__} must override sample() or inverse_cdf().")
