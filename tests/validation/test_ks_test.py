from sdatools.distributions.continuous.normal import NormalDistribution
from sdatools.distributions.continuous.uniform import UniformDistribution
from sdatools.validation.goodness_of_fit.ks_test import KSTest

import numpy as np


def test_ks_test_on_normal_data():
    data = np.random.normal(0, 1, 200)
    ks = KSTest(data)
    ks.test(dist=NormalDistribution(0, 1))
    assert ks.result == "PASS"


def test_ks_test_on_uniform_data():
    data = np.random.uniform(0, 1, 100)
    ks = KSTest(data)
    ks.test(dist=UniformDistribution(0, 1))
    assert ks.result == "PASS"
