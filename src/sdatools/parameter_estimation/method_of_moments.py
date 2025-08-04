from sdatools.distributions.base_distribution import Distribution

from sdatools.distributions.continuous.normal import NormalDistribution
from sdatools.distributions.continuous.gamma import GammaDistribution
from sdatools.distributions.continuous.exponential import ExponentialDistribution


class MethodOfMoments:
    """
    A class to perform parameter estimation using the Method of Moments

    Inputs:
        data: A list of observed data points

    Methods:
        calculate_moments(): Calculates the sample moments of the data
        fit(): Estimates the parameters of the distribution using the method of moments
    """

    def __init__(self, data):
        self.data = data
        self.moments: tuple = self.calculate_sample_moments()


    def calculate_sample_moments(self):
        """
        Calculates the sample moments of the data

        Returns:
            tuple: A tuple containing mean, variance, skewness, and kurtosis
        """
        n = len(self.data)
        mean = sum(self.data) / n
        variance = sum((x - mean) ** 2 for x in self.data) / n
        skewness = sum((x - mean) ** 3 for x in self.data) / (n * (variance ** 1.5))
        kurtosis = sum((x - mean) ** 4 for x in self.data) / (n * (variance ** 2)) - 3

        return (mean, variance, skewness, kurtosis)


    def fit(self, dist: Distribution) -> Distribution:
        """
        Estimates the parameters of the distribution using the Method of Moments

        Args:
            dist (Distribution): The distribution to fit

        Returns:
            Distribution: The fitted distribution with estimated parameters
        """

        if isinstance(dist, NormalDistribution):
            mu = self.moments[0]
            sigma = self.moments[1] ** 0.5
            return NormalDistribution(mu=mu, sigma=sigma)
        
        elif isinstance(dist, GammaDistribution):
            alpha = self.moments[0]**2 / self.moments[1]
            beta = self.moments[1] / self.moments[0]
            return GammaDistribution(alpha=alpha, beta=beta)
        
        elif isinstance(dist, ExponentialDistribution):
            lam = 1 / self.moments[0]
            return ExponentialDistribution(lam=lam)
        
        else:
            Exception("Unsupported distribution type for method of moments fitting.")
            return dist
