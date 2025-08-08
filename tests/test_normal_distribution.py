from sdatools.distributions import NormalDistribution


# Special methods

def test_normal_distribution_addition():
    dist1, dist2 = trial_normal_distributions()
    dist_sum = dist1 + dist2
    assert dist_sum.mu == 8  # 5 + 3
    assert dist_sum.sigma == (2**2 + 4**2)**0.5  # sqrt(2^2 + 4^2)

def test_normal_distribution_subtraction():
    dist1, dist2 = trial_normal_distributions()
    dist_diff = dist1 - dist2
    assert dist_diff.mu == 2  # 5 - 3
    assert dist_diff.sigma == (2**2 + 4**2)**0.5  # sqrt(2^2 + 4^2)

def test_normal_distribution_scalar_multiplication():
    dist1, _ = trial_normal_distributions()
    dist_scaled = 3 * dist1
    assert dist_scaled.mu == 15  # 3 * 5
    assert dist_scaled.sigma == 6  # 3 * 2

def test_normal_distribution_scalar_division():
    dist1, _ = trial_normal_distributions()
    dist_divided = dist1 / 2
    assert dist_divided.mu == 2.5  # 5 / 2
    assert dist_divided.sigma == 1.0  # 2 / 2

def test_normal_distribution_equality():
    dist1, dist2 = trial_normal_distributions()
    assert dist1 != dist2
    assert not (dist1 == dist2)


# Helper functions

def trial_normal_distributions():
    return NormalDistribution(mu=5, sigma=2), NormalDistribution(mu=3, sigma=4)
