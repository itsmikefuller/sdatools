from sdatools.numerical_methods.quadrature.abstract.quadrature_rule import QuadratureRule

from typing import Callable


class SimpsonRule(QuadratureRule):
    """
    Quadratic quadrature rule using Simpson's method
    
    The approximation is exact for cubic functions
    """
    @property
    def order(self) -> int:
        return 2
    
    @property
    def exact_order(self) -> int:
        return 3
    
    def integrate(self, f: Callable, a: float, b: float) -> float:
        h = (b - a) / 2
        return h / 3 * (f(a) + 4 * f((a + b) / 2) + f(b))


class Simpson38Rule(QuadratureRule):
    """
    Cubic quadrature rule using Simpson's 3/8 method

    The approximation is exact for cubic functions
    """
    @property
    def order(self) -> int:
        return 3
    
    @property
    def exact_order(self) -> int:
        return 3
    
    def integrate(self, f: Callable, a: float, b: float) -> float:
        h = (b - a) / 3
        return 3 * h / 8 * (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(b))
