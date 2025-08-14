import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

from sdatools.core.types import SeriesLike
from sdatools.distributions.abstract.continuous_distribution import ContinuousDistribution


class KSTest:
    """
    A class to perform the Kolmogorov-Smirnov test for goodness of fit between
    the empirical distribution of a sample and a specified theoretical distribution
    
    Inputs:
        data (SeriesLike): the sample data to test
    
    Methods:
        test: performs the Kolmogorov-Smirnov test against a specified distribution
        get_ks_statistic: returns the KS statistic from the last test performed
        get_p_value: returns the p-value from the last test performed
    """

    def __init__(self, data: SeriesLike):
        self._data = np.sort(data)
        self._n = len(self._data)
        self._fig, self._ax = plt.subplots()

    @property
    def ks_statistic(self) -> float:
        return self._ks_statistic
    
    @property
    def p_value(self) -> float:
        return self._p_value
    
    @property
    def result(self) -> str:
        return self._result
    
    # TODO: Implement KS test
    def test(self, dist: ContinuousDistribution, alpha: float = 0.05):
        """
        Perform the Kolmogorov-Smirnov test against a specified distribution.
        
        Args:
            dist (type[Distribution] or Distribution): a distribution to compare against
        """ 
        empirical_cdf = self._empirical_cdf()
        theoretical_cdf = np.array([dist.cdf(x) for x in self._data])

        # Compute KS statistic
        self._ks_statistic = np.max(np.abs(empirical_cdf - theoretical_cdf))
        print(f"KS statistic: {self._ks_statistic:.8f}")

        # Compute p-value
        self._p_value = self._get_p_value(self._ks_statistic)
        print(f"p-value: {self._p_value:.8f}")

        # Test result
        if self._p_value >= alpha:
            print(f"KS test against {dist.__class__.__name__} PASSED")
            self._result = "PASS"
        else:
            print(f"KS test against {dist.__class__.__name__} FAILED")
            self._result = "FAIL"

        self._plot_ks_test_result(dist, alpha)
        
    
    def _empirical_cdf(self) -> np.ndarray:
        """Create an array of empirical CDF y-values."""
        return np.arange(1, self._n + 1) / self._n
    

    def _get_p_value(self, ks_stat: float) -> float:
        """Compute p-value using asymptotic approximation of Kolmogorov Distribution."""
        sqrt_n = sqrt(self._n)
        lam = (sqrt_n + 0.12 + 0.11 / sqrt_n) * ks_stat
        p_value = 2 * sum(
            (-1) ** (k - 1) * exp(-2 * (lam ** 2) * (k ** 2))
            for k in range(1, 100)
        )
        return max(min(p_value, 1.0), 0.0)
    

    def _plot_ks_test_result(self, 
            dist: ContinuousDistribution,
            alpha: float,
            color_empirical: str = 'k',
            color_theoretical: str = 'b',
            linestyle: str = '-',
            lw: int = 2):
        """
        Plot the empirical CDF versus the theoretical CDF
        """
        
        # Empirical CDF (step function)
        empirical_cdf_x_values = self._data
        empirical_cdf_y_values = self._empirical_cdf()
        self._ax.step(
            empirical_cdf_x_values,
            empirical_cdf_y_values,
            color=color_empirical,
            linestyle=linestyle,
            lw=lw,
            label='Empirical CDF'
        )

        # Theoretical CDF
        theoretical_cdf_y_values = [dist.cdf(x) for x in empirical_cdf_x_values]
        self._ax.plot(
            empirical_cdf_x_values,
            theoretical_cdf_y_values,
            color=color_theoretical,
            linestyle=linestyle,
            lw=lw,
            label='Theoretical CDF'
        )

        self._ax.set_xlabel("x")
        self._ax.set_ylabel("CDF")
        self._ax.set_title(f"KS test against {dist.__class__.__name__} ($\\alpha$={alpha})")
        self._ax.legend()

        plt.show()
