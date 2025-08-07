from sdatools.distributions import NormalDistribution, GammaDistribution, ExponentialDistribution
from sdatools.parameter_estimation.method_of_moments import MethodOfMoments

from math import isclose


def test_method_of_moments_normal():

    # Example data from N(4, 3**2) distribution
    data = [5.49, 3.59, 5.94, 8.57, 3.3, 3.3, 8.74, 6.3, 2.59, 5.63, 2.61, 2.6, 4.73, -1.74, -1.17, 2.31, 0.96, 4.94, 1.28, -0.24, 8.4, 3.32, 4.2, -0.27, 2.37, 4.33, 0.55, 5.13, 2.2, 3.12, 2.19, 9.56, 3.96, 0.83, 6.47, 0.34, 4.63, -1.88, 0.02, 4.59, 6.22, 4.51, 3.65, 3.1, -0.44, 1.84, 2.62, 7.17, 5.03, -1.29, 4.97, 2.84, 1.97, 5.84, 7.09, 6.79, 1.48, 3.07, 4.99, 6.93, 2.56, 3.44, 0.68, 0.41, 6.44, 8.07, 3.78, 7.01, 5.08, 2.06, 5.08, 8.61, 3.89, 8.69, -3.86, 6.47, 4.26, 3.1, 4.28, -1.96, 3.34, 5.07, 8.43, 2.45, 1.57, 2.49, 6.75, 4.99, 2.41, 5.54, 4.29, 6.91, 1.89, 3.02, 2.82, -0.39, 4.89, 4.78, 4.02, 3.3]
    mean = 3.6883000000000004
    stddev = 2.71092716796302
    
    # Fit a NormalDistribution
    mom = MethodOfMoments(data)
    fitted_dist = mom.fit(NormalDistribution())
    
    # Check the estimated parameters
    assert isclose(fitted_dist.mean(), mean)
    assert isclose(fitted_dist.stddev(), stddev)


def test_method_of_moments_exponential():

    # Example data
    data = [1, 2, 3, 4, 5]
    mean = 3
    
    # Fit an ExponentialDistribution
    mom = MethodOfMoments(data)
    fitted_dist = mom.fit(ExponentialDistribution())
    
    # Check an Exponential distribution has been fitted
    assert isinstance(fitted_dist, ExponentialDistribution)

    # Check the estimated parameters
    assert fitted_dist.lam == (1 / mean)  # lambda = inverse of the mean


def test_method_of_moments_gamma():

    # Example data
    data = [1, 2, 3, 4, 5]
    mean = 3
    variance = 2
    
    # Fit a GammaDistribution
    mom = MethodOfMoments(data)
    fitted_dist = mom.fit(GammaDistribution())
    
    # Check a Gamma distribution has been fitted
    assert isinstance(fitted_dist, GammaDistribution)

    # Check the estimated parameters
    assert fitted_dist.alpha == 4.5  # alpha = mean**2 / variance
    assert fitted_dist.beta == 2 / 3  # beta = variance / mean
