import numpy as np
import pandas as pd
from functools import wraps
from typing import Callable

from sdatools.core.types import NumericLike, SeriesLike


def vectorise_input(func: Callable) -> Callable:
    """
    Decorator to apply a scalar-only function elementwise across common array-like types
    
    Supports NumericLike inputs (see sdatools.core.types.NumericLike)
    """
    @wraps(func)
    def wrapper(x, *args, **kwargs):
        if np.isscalar(x):
            return func(x, *args, **kwargs)
        
        if isinstance(x, np.ndarray):
            return np.array([func(xi, *args, **kwargs) for xi in x])
        
        if isinstance(x, pd.Series):
            return x.apply(lambda xi: func(xi, *args, **kwargs))
        
        if isinstance(x, pd.DataFrame):
            return x.map(lambda xi: func(xi, *args, **kwargs))

        raise TypeError(f"Unsupported input type: {type(x)}")
        
    return wrapper


def min_SeriesLike(data: SeriesLike) -> float:
    """
    Calculate the minimum of a SeriesLike object
    
    Args:
        data (SeriesLike): Input data, which can be a list, numpy array, or pandas series
        
    Returns:
        float: (min, max) of the input data
    """
    if isinstance(data, list):
        data = np.array(data)
    
    if isinstance(data, np.ndarray):
        return np.min(data)
    
    elif isinstance(data, pd.Series):
        return data.min()
    
    else:
        raise TypeError(f"Unsupported data type: {type(data)}")
    

def max_SeriesLike(data: SeriesLike) -> float:
    """
    Calculate the maximum of a SeriesLike object
    
    Args:
        data (SeriesLike): Input data, which can be a list, numpy array, or pandas series
        
    Returns:
        float: (min, max) of the input data
    """
    neg_min = min_SeriesLike(data * -1)
    return -neg_min


# Validation helper functions

def validate_probability(p: float) -> None:
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be in the range [0, 1].")
