import matplotlib
import matplotlib.pyplot as plt


class Histogram:
    """
    A class for creating and displaying histograms from data
    """

    def __init__(self, data: list, bins: int = 50):
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Data must be a list.")
        self.data = data
        self.bins = bins
        self._fig, self._ax = plt.subplots()


    def plot(self, 
             title: str = "Histogram",
             xlabel: str = "Value",
             ylabel: str = "Density"):
        """
        Plot the histogram of the initialised data
        """
        self._ax.hist(self.data, bins=self.bins, density=True, edgecolor='black', alpha=0.6)

        self._ax.set_title(title)
        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)


    # TODO: Add type hints for x_values and pdf
    def overlay_pdf(self, 
                    x_values,
                    pdf,
                    color: str = 'k',
                    linestyle: str = '-',
                    lw: int = 2):
        """
        Overlay a PDF on the histogram
        """
        self._ax.plot(x_values, pdf, color=color, linestyle=linestyle, lw=lw, label='PDF')
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
    