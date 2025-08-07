from typing import Union
import numpy as np
import pandas as pd


# sdatools global type for numeric values
NumericLike = Union[int, float, np.ndarray, pd.Series, pd.DataFrame]

# sdatools global type for 1D arrays
SeriesLike = Union[list[int], list[float], np.ndarray, pd.Series]
