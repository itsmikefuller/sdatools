from sdatools.core.types import SeriesLike
from sdatools.distributions import Distribution

import numpy as np


class KolmogorovSmirnovTest:
    """
    A class to perform the Kolmogorov-Smirnov test for goodness of fit between
    the empirical distribution of a sample and a specified theoretical distribution
    
    Inputs:
        data: array-like, the sample data to test
    
    Methods:
        test: performs the Kolmogorov-Smirnov test against a specified distribution
        get_ks_statistic: returns the KS statistic from the last test performed
        get_p_value: returns the p-value from the last test performed
    """

    def __init__(self, data: SeriesLike):
        self.data = data
        self.n = len(self.data)
        self.ks_statistic = None
        self.p_value = None

    
    # TODO: Implement KS test
    def test(self, dist: Distribution):
        """
        Perform the Kolmogorov-Smirnov test against a specified distribution
        
        Args:
            dist (Distribution): a distribution to compare against
        """
        if not isinstance(dist, Distribution):
            raise ValueError("dist must be an instance of Distribution")
        raise NotImplementedError("KS test not yet implemented.")
        
    
    # TODO: Implement make empirical distribution function, if it is useful for KS test
    def _make_empirical_distribution(self):
        """
        Create an empirical distribution from the sample data
        """
        pass


    def get_ks_statistic(self):
        return self.ks_statistic
    

    def get_p_value(self):
        return self.p_value
