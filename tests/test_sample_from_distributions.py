from sdatools.distributions.discrete.binomial import BinomialDistribution
from sdatools.distributions.discrete.poisson import PoissonDistribution


def test_sample_binomial():
    """Test sampling from a Binomial distribution."""
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
    """Test sampling from a Poisson distribution."""
    lam = 4.0
    poisson_dist = PoissonDistribution(lam)
    
    # Sample size of 5
    sample_size = 5
    sample = poisson_dist.sample(sample_size)
    
    # Check if the sample is of the correct size
    assert len(sample) == sample_size
    
    # Check if all samples are non-negative integers
    assert all(isinstance(x, int) and x >= 0 for x in sample)


def test_sample_invalid_size():
    """Test sampling with invalid sample size."""
    n = 10
    p = 0.5
    binomial_dist = BinomialDistribution(n, p)
    
    # Test with negative sample size
    try:
        binomial_dist.sample(-1)
    except ValueError as e:
        assert str(e) == "Sample size must be a positive integer."
    
    # Test with non-integer sample size
    try:
        binomial_dist.sample(2.5)
    except ValueError as e:
        assert str(e) == "Sample size must be an integer."


# Run the tests
test_sample_binomial()
test_sample_poisson()
test_sample_invalid_size()
