import pytest

from sdatools.distributions.discrete.binomial import BinomialDistribution
from sdatools.distributions.discrete.poisson import PoissonDistribution
from sdatools.distributions.continuous.normal import NormalDistribution


def test_sample_binomial():
    """
    Test sampling from a Binomial distribution
    """
    n = 10
    p = 0.5
    binomial_dist = BinomialDistribution(n, p)
    
    # Sample size of 5
    sample_size = 5
    sample = binomial_dist.sample(sample_size)
    
    # Check if the sample is of the correct size
    assert len(sample) == sample_size
    
    # Check if all samples are within the valid range [0, n]
    assert all(0 <= x <= n for x in sample)


def test_sample_poisson():
    """
    Test sampling from a Poisson distribution
    """
    lam = 4.0
    poisson_dist = PoissonDistribution(lam)
    
    # Sample size of 5
    sample_size = 5
    sample = poisson_dist.sample(sample_size)
    
    # Check if the sample is of the correct size
    assert len(sample) == sample_size
    
    # Check if all samples are non-negative integers
    assert all(isinstance(x, int) and x >= 0 for x in sample)


def test_sample_normal():
    """
    Test sampling from a Normal distribution
    """
    mus = [-1, 0, 2.5]
    sigmas = [0.1, 1, 3] 
    sample_sizes = [1, 5, 100]

    for mu, sigma in zip(mus, sigmas):
        normal_dist = NormalDistribution(mu, sigma)
        
        for sample_size in sample_sizes:
            samples = normal_dist.sample(sample_size)
            
            # Check if the sample is of the correct size
            assert len(samples) == sample_size
            
            # TODO: determine other checks


def test_sample_negative_size():
    """
    Test sampling with negative sample size
    """
    binomial_dist = BinomialDistribution(10, 0.5)
    with pytest.raises(ValueError, match="Sample size must be a positive integer."):
        binomial_dist.sample(-1)
