from sdatools.statistics.qq_plot import QQPlot


def test_qq_plot_uniform():
    """Test the QQPlot class with a Uniform(0, 1) distribution."""
    from sdatools.distributions.continuous.uniform import UniformDistribution
    import numpy as np

    # Create a uniform distribution
    uniform_dist = UniformDistribution(0, 1)

    # Generate theoretical quantiles for the uniform distribution
    theoretical_quantiles = np.linspace(0, 1, 100)

    # Generate sample quantiles from the uniform distribution
    # TODO: Replace with actual sample quantiles from UniformDistribution class
    sample_quantiles = np.random.uniform(0, 1, 100)

    # Create a QQPlot instance
    qq_plot = QQPlot(theoretical_distribution=uniform_dist)

    # Plot the QQ plot
    qq_plot.plot(theoretical_quantiles, sample_quantiles, show_plot=True)


def test_qq_plot_normal():
    """Test the QQPlot class with a standard Normal distribution."""
    from sdatools.distributions.continuous.normal import NormalDistribution
    import numpy as np

    # Create a normal distribution
    normal_dist = NormalDistribution(0, 1)

    # Generate theoretical quantiles for the normal distribution
    theoretical_quantiles = np.linspace(-3, 3, 100)

    # Generate sample quantiles from the normal distribution
    # TODO: Replace with actual sample quantiles from NormalDistribution class
    sample_quantiles = np.random.normal(0, 1, 100)

    # Create a QQPlot instance
    qq_plot = QQPlot(theoretical_distribution=normal_dist)

    # Plot the QQ plot
    qq_plot.plot(theoretical_quantiles, sample_quantiles, show_plot=True)
