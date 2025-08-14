from sdatools.data_visualisation.qq_plot import QQPlot
from sdatools.distributions.continuous.uniform import UniformDistribution
from sdatools.distributions.continuous.normal import NormalDistribution

import numpy as np
import datetime


def test_qq_plot_uniform():
    """
    Test the QQPlot class with a Uniform(0, 1) distribution
    """
    
    # Create a uniform distribution
    uniform_dist = UniformDistribution(0, 1)

    # Generate sample quantiles from the uniform distribution
    sample_quantiles = uniform_dist.sample(100)
    sample_quantiles.sort()

    # Generate theoretical quantiles for the uniform distribution
    probs = np.linspace(0.01, 0.99, 100)
    theoretical_quantiles: list[float] = [uniform_dist.inverse_cdf(p) for p in probs]
    theoretical_quantiles.sort()

    # Create a QQPlot instance
    qq_plot = QQPlot(theoretical_distribution=uniform_dist)

    # Plot the QQ plot
    qq_plot.plot(theoretical_quantiles, sample_quantiles, show_plot=True)


def test_qq_plot_normal():
    """
    Test the QQPlot class with a standard Normal distribution
    """

    # Create a normal distribution
    normal_dist = NormalDistribution(0, 1)

    # Generate sample quantiles from the normal distribution
    sample_quantiles = normal_dist.sample(100)
    sample_quantiles.sort()

    # Generate theoretical quantiles for the normal distribution
    probs = np.linspace(0.01, 0.99, 100)
    theoretical_quantiles = [normal_dist.inverse_cdf(p) for p in probs]
    theoretical_quantiles.sort()

    # Create a QQPlot instance
    qq_plot = QQPlot(theoretical_distribution=normal_dist)

    # Plot the QQ plot
    qq_plot.plot(theoretical_quantiles, sample_quantiles, show_plot=True)

    # Save the figure
    # Check image manually for correctness!
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")
    qq_plot.save_fig(f'tests/_images/{timestamp}_test_qq_plot_normal.png')
