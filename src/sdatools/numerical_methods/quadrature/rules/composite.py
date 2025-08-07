from sdatools.numerical_methods.quadrature import QuadratureRule

from typing import Callable


class CompositeRule(QuadratureRule):
    """
    Composite quadrature rule that applies a specified quadrature rule over multiple subintervals
    """
    def __init__(self, rule: QuadratureRule, num_subintervals: int):
        self.rule = rule
        if num_subintervals < 1:
            raise ValueError("Number of subintervals must be at least 1.")
        self.num_subintervals = num_subintervals

    @property
    def order(self) -> int:
        return self.rule.order
    
    @property
    def exact_order(self) -> int:
        return self.rule.exact_order
    
    def integrate(self, f: Callable, a: float, b: float) -> float:
        subinterval_width = (b - a) / self.num_subintervals
        integral = 0.0
        x_lower = a
        for _ in range(self.num_subintervals):
            x_upper = x_lower + subinterval_width
            integral += self.rule.integrate(f, x_lower, x_upper)
            x_lower = x_upper
        return integral
    