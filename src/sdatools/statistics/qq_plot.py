import matplotlib.pyplot as plt
import numpy as np

from sdatools.distributions.base_distribution import Distribution


class QQPlot:
    '''
    Class for creating quantile-quantile plots.
    
    Args:
        theoretical_distribution (Distribution): The theoretical distribution to compare against.
    
    Methods:
        plot(theoretical_quantiles, sample_quantiles): Plots the quantiles of the sample against the theoretical quantiles.
    '''
    def __init__(self, theoretical_distribution: Distribution):
        self.theoretical_distribution = theoretical_distribution

    def plot(self, theoretical_quantiles, sample_quantiles, show_plot: bool = False):
        '''Plot the quantiles of the sample against the theoretical quantiles.'''
        # Ensure that theoretical_quantiles and sample_quantiles are numpy arrays
        theoretical_quantiles = np.asarray(theoretical_quantiles)
        sample_quantiles = np.asarray(sample_quantiles)

        # Create the QQ plot
        plt.figure(figsize=(8, 8))
        plt.scatter(theoretical_quantiles, sample_quantiles, color='blue', label='Sample Quantiles')
        
        # Add a 45-degree line for reference
        max_val = max(np.max(theoretical_quantiles), np.max(sample_quantiles))
        min_val = min(np.min(theoretical_quantiles), np.min(sample_quantiles))
        plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='y=x Line')

        plt.title('Quantile-Quantile Plot')
        plt.xlabel('Theoretical Quantiles')
        plt.ylabel('Sample Quantiles')
        plt.legend()
        plt.grid()
        if show_plot: plt.show() 
        return plt

    def check_distribution(self, sample_quantiles):
        '''Check if the sample quantiles follow the theoretical distribution.'''
        # TODO: This method can be implemented to perform statistical tests like Kolmogorov-Smirnov test
        # or Shapiro-Wilk test to check if the sample follows the theoretical distribution.
        pass
