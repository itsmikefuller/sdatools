import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from sdatools.core.types import SeriesLike
from sdatools.core.utils import max_SeriesLike, min_SeriesLike
from sdatools.distributions import ContinuousDistribution


class Histogram:
    """
    A class for creating and displaying histograms from data
    """

    def __init__(self,
            data: SeriesLike,
            bins: int = 50
            ):
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Data must be numeric")
        self.data: np.ndarray = np.asarray(data)
        self.min: float = min_SeriesLike(data)
        self.max: float = max_SeriesLike(data)
        self.bins: int = bins
        self._fig, self._ax = plt.subplots()


    def plot_data(self, 
             title: str = "Histogram",
             xlabel: str = "Value",
             ylabel: str = "Density"):
        """
        Plot the histogram with the initialised data
        """
        self._ax.hist(self.data, bins=self.bins, density=True, edgecolor='black', alpha=0.6)

        self._ax.set_title(title)
        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)


    def overlay_pdf(self, 
                    distribution: ContinuousDistribution,
                    color: str = 'k',
                    linestyle: str = '-',
                    lw: int = 2):
        """
        Overlay the PDF of the given distribution on the histogram
        """
        pdf_x_values: np.ndarray = np.linspace(self.min, self.max, 100)
        pdf_y_values: np.ndarray = np.asarray([distribution.pdf(val) for val in pdf_x_values])
        self._ax.plot(
            pdf_x_values,
            pdf_y_values,
            color=color,
            linestyle=linestyle,
            lw=lw,
            label='PDF'
        )
        plt.draw()

    
    def show(self):
        """
        Show the histogram plot: works with both inline (e.g. Jupyter) and GUI backends
        """
        backend = matplotlib.get_backend()
        if backend == 'module://matplotlib_inline.backend_inline':
            # Jupyter inline backend
            plt.show()
        else:
            # GUI backend (e.g., TkAgg, Qt5Agg)
            self._fig.show()


    def save_fig(self, filename: str):
        self._fig.savefig(filename)
    