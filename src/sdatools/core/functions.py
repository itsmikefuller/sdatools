import numpy as np

from sdatools.core.utils import vectorise_input


@vectorise_input
def erf(x: float) -> float:
    """
    Calculate the error function using a numerical approximation

    The approximation is based on the Abramowitz and Stegun formula
    """
    if x == 0:
        return 0.0
    if x < 0:
        return -erf(-x)
    if x > 6:
        return 1.0
    if x < 1e-10:
        return x
    
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p = 0.3275911
    
    t = 1 / (1 + p * x)
    return 1 - (a1 * t + a2 * t**2 + a3 * t**3 + a4 * t**4 + a5 * t**5) * np.exp(-x**2)


@vectorise_input
def phi(x: float) -> float:
    """
    Calculate the standard normal PDF (phi function)
    """
    return (1.0 / (np.sqrt(2.0 * np.pi))) * np.exp(-0.5 * x ** 2)


@vectorise_input
def Phi(x: float) -> float:
    """
    Calculate the standard normal CDF (Phi function)
    
    Uses the error function for numerical approximation
    """
    return 0.5 * (1 + erf(x / np.sqrt(2)))
