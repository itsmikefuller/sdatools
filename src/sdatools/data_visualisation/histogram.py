import matplotlib.pyplot as plt
import scipy.stats as stats


class Histogram:
    """
    A class for creating and displaying histograms from data
    """

    def __init__(self, data: list):
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Data must be a list.")
        self.data = data
        self._fig, self._ax = plt.subplots()


    def plot(self):
        """
        Plot the histogram of the initialised data
        """
        self._ax.hist(self.data, density=True, edgecolor='black', alpha=0.6)

        self._ax.set_title('Histogram')
        self._ax.set_xlabel('Value')
        self._ax.set_ylabel('Density')

        plt.show()


    # TODO: Add type hints for x_values and pdf
    def overlay_pdf(self, x_values, pdf):
        """
        Overlay a PDF on the histogram
        """
        self._ax.plot(x_values, pdf, 'k-', lw=2)
        plt.draw()


    def save_fig(self, filename: str):
        self._fig.savefig(filename)
    