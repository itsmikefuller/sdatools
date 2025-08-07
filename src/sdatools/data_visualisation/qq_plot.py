import matplotlib.pyplot as plt
import numpy as np

from sdatools.distributions import Distribution


class QQPlot:
    '''
    Class for creating quantile-quantile plots.
    
    Inputs:
        theoretical_distribution (Distribution): The theoretical distribution to compare against.
    
    Methods:
        plot(theoretical_quantiles, sample_quantiles): Plots the quantiles of the sample against the theoretical quantiles.
    '''
    def __init__(self, theoretical_distribution: Distribution):
        self.theoretical_distribution = theoretical_distribution
        self._fig, self._ax = plt.subplots(figsize=(8, 8))

    def plot(self, theoretical_quantiles, sample_quantiles, show_plot: bool = False):
        '''Plot the quantiles of the sample against the theoretical quantiles.'''
        # Check that theoretical_quantiles and sample_quantiles are numpy arrays
        theoretical_quantiles = np.asarray(theoretical_quantiles)
        sample_quantiles = np.asarray(sample_quantiles)

        # Clear any previous content
        self._ax.clear()

        # Create the QQ plot
        self._ax.scatter(theoretical_quantiles, sample_quantiles, color='blue', label='Sample Quantiles')
        
        # Add y=x line
        max_val = max(np.max(theoretical_quantiles), np.max(sample_quantiles))
        min_val = min(np.min(theoretical_quantiles), np.min(sample_quantiles))
        self._ax.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='y=x Line')

        # Set labels and title
        self._ax.set_title('Quantile-Quantile Plot')
        self._ax.set_xlabel('Theoretical Quantiles')
        self._ax.set_ylabel('Sample Quantiles')
        self._ax.legend()
        self._ax.grid(True)

        if show_plot: 
            plt.show() 

        return self._fig
    
    def save_fig(self, filename: str):
        self._fig.savefig(filename)
