from math import sinh, sqrt, isfinite
import numpy as np
import pytest

from sdatools.core.constants import EXP_LIMIT
from sdatools.distributions import JohnsonSUDistribution


# Fixtures
# TODO: Check pytest docs for cleaner way to implement tests using single and multiple fixtures

def jsu_dist1() -> JohnsonSUDistribution:
    """
    g(z) = sinh(z)
    
    Expect zero mean, no skew
    """
    (gamma, delta, xi, lam) = (0.0, 1.0, 0.0, 1.0)
    return JohnsonSUDistribution(gamma, delta, xi, lam)

def jsu_dist2() -> JohnsonSUDistribution:
    """
    g(z) = 0.5 + 1.5 * sinh((x - 1) / 2)
    
    Expect negative skew, lighter tails
    """
    (gamma, delta, xi, lam) = (1.0, 2.0, 0.5, 1.5)
    return JohnsonSUDistribution(gamma, delta, xi, lam)

def jsu_dist3() -> JohnsonSUDistribution:
    """
    g(z) = 1 + 2 * sinh((x + 0.5) / 0.8)
    
    Expect positive skew, heavier tails
    """
    (gamma, delta, xi, lam) = (-0.5, 0.8, 1.0, 2.0)
    return JohnsonSUDistribution(gamma, delta, xi, lam)


# Init and parameter validation

def test_invalid_delta():
    with pytest.raises(ValueError):
        JohnsonSUDistribution(delta=0)

def test_invalid_lam():
    with pytest.raises(ValueError):
        JohnsonSUDistribution(lam=0)

def test_exp_overflow_guard():
    # Choose delta such that (1 / delta ** 2) > EXP_LIMIT
    delta = 1 / sqrt(EXP_LIMIT + 1)
    jsu = JohnsonSUDistribution(delta=delta)
    assert jsu._expdmin2 == float("inf")


# Distribution properties

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_mean_finite(dist):
    assert isfinite(dist.mean)

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_variance_finite(dist):
    assert isfinite(dist.variance)

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_skewness_finite(dist):
    assert isfinite(dist.skewness)

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_kurtosis_finite(dist):
    assert isfinite(dist.kurtosis)

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_variance_positive(dist):
    assert dist.variance > 0

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_pdf_positive(dist):
    domain = np.linspace(-5, 5, 100)
    assert all(dist.pdf(x) for x in domain)

@pytest.mark.parametrize('dist', [jsu_dist1(), jsu_dist2(), jsu_dist3()])
def test_cdf_monotonic(dist):
    domain = np.linspace(-5, 5, 100)
    cdf = [dist.cdf(x) for x in domain]
    assert all(cdf[i] <= cdf[i+1] for i in range(len(cdf)-1))
    assert 0 <= cdf[0] <= 1
    assert 0 <= cdf[-1] <= 1
    

# Specific fixture properties

def test_jsu_dist1_properties(dist=jsu_dist1()):
    assert dist.mean == 0
    assert dist.skewness == 0

def test_jsu_dist2_properties(dist=jsu_dist2()):
    assert dist.skewness < 0

def test_jsu_dist3_properties(dist=jsu_dist3()):
    assert dist.skewness > 0
