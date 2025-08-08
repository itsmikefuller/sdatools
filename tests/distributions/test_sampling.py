import pytest

from sdatools.distributions import BinomialDistribution, PoissonDistribution


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


def test_sample_negative_size():
    """
    Test sampling with negative sample size
    """
    binomial_dist = BinomialDistribution(10, 0.5)
    with pytest.raises(ValueError, match="Sample size must be a positive integer."):
        binomial_dist.sample(-1)
