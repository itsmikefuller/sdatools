from math import exp

def erf(x: float) -> float:
    """Calculate the error function using a numerical approximation."""
    if x < 0:
        return -erf(-x)
    if x == 0:
        return 0.0
    if x > 6:
        return 1.0
    if x < 1e-10:
        return x
    
    sign = 1 if x >= 0 else -1
    x = abs(x)
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p = 0.3275911
    
    t = 1 / (1 + p * x)
    return sign * (1 - (a1 * t + a2 * t**2 + a3 * t**3 + a4 * t**4 + a5 * t**5) * exp(-x**2))
