from sdatools.numerical_methods.quadrature import QuadratureRule

from typing import Callable


class BooleRule(QuadratureRule):
    """
    Quartic quadrature rule using Boole's method

    The approximation is exact for quintic functions
    """
    @property
    def order(self) -> int:
        return 4
    
    @property
    def exact_order(self) -> int:
        return 5
    
    def integrate(self, f: Callable, a: float, b: float) -> float:
        h = (b - a) / 4
        return 2 * h / 45 * (7 * f(a) + 32 * f(a + h) + 12 * f(a + 2 * h) + 32 * f(a + 3 * h) + 7 * f(b))
