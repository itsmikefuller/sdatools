from sdatools.numerical_methods.quadrature.abstract.quadrature_rule import QuadratureRule

from typing import Callable


class TrapeziumRule(QuadratureRule):
    """
    Linear quadrature rule
    
    The approximation is exact for linear functions
    """
    @property
    def order(self) -> int:
        return 1
    
    @property
    def exact_order(self) -> int:
        return 1
    
    def integrate(self, f: Callable, a: float, b: float) -> float:
        return (b - a) / 2 * (f(a) + f(b))
    