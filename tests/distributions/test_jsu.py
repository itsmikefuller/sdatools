from math import sinh

from sdatools.distributions import JohnsonSUDistribution


# TODO: check how transformation of distributions affects moments
def test_jsu_moments():
    jsu = JohnsonSUDistribution(gamma=0, delta=1, xi=0, lam=1) # z = arcsinh(x), z ~ N(0,1)
    print(jsu.mean)
    # print(jsu.variance)
    # print(jsu.skewness)
    # print(jsu.kurtosis)
    
    assert jsu.mean == sinh(0)
    # assert jsu.variance == sinh(1)
