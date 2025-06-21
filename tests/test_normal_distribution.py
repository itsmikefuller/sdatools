from sdatools.distributions.continuous.normal import NormalDistribution


def test_normal_distribution_operations():
    """Test operations on NormalDistribution instances."""
    # Create two normal distributions
    dist1 = NormalDistribution(mu=5, sigma=2)
    dist2 = NormalDistribution(mu=3, sigma=4)

    # Test addition
    dist_sum = dist1 + dist2
    assert dist_sum.mu == 8  # 5 + 3
    assert dist_sum.sigma == (2**2 + 4**2)**0.5  # sqrt(2^2 + 4^2)

    # Test subtraction
    dist_diff = dist1 - dist2
    assert dist_diff.mu == 2  # 5 - 3
    assert dist_diff.sigma == (2**2 + 4**2)**0.5  # sqrt(2^2 + 4^2)

    # Test scalar multiplication
    dist_scaled = 3 * dist1
    assert dist_scaled.mu == 15  # 3 * 5
    assert dist_scaled.sigma == 6  # 3 * 2

    # Test scalar division
    dist_divided = dist1 / 2
    assert dist_divided.mu == 2.5  # 5 / 2
    assert dist_divided.sigma == 1.0  # 2 / 2

    # Test equality and inequality
    assert dist1 != dist2
    assert not (dist1 == dist2)
