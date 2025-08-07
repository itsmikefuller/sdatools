from math import isclose
from typing import Callable

from sdatools.numerical_methods.quadrature import (
    TrapeziumRule,
    SimpsonRule,
    Simpson38Rule,
    BooleRule,
    QuadratureRule
)

# Tests

def test_trapezium_rule_exact_on_linear_functions():
    """
    Test that the trapezium rule is exact for a selection of linear functions
    """
    trapezium_rule = TrapeziumRule()
    check_linear_functions(trapezium_rule)


def test_simpson_rule_exact_on_cubic_functions():
    """
    Test that the Simpson rule is exact for a selection of cubic functions
    """
    simpson_rule = SimpsonRule()
    check_cubic_functions(simpson_rule)


def test_simpson_38_rule_exact_on_cubic_functions():
    """
    Test that the Simpson 3/8 rule is exact for a selection of cubic functions
    """
    simpson_38_rule = Simpson38Rule()
    check_cubic_functions(simpson_38_rule)


def test_boole_rule_exact_on_quintic_functions():
     """
     Test that the Boole rule is exact for a selection of quintic functions
     """
     boole_rule = BooleRule()
     check_quintic_functions(boole_rule)


# Helper functions

def check_linear_functions(rule: QuadratureRule):
    """
    Check that the input quadrature rule is exact for a selection of linear functions
    """
    def exact_integral_linear(a: float, b: float, min: float, max: float) -> float:
        F: Callable = lambda x: (a / 2) * x ** 2 + b * x
        return F(max) - F(min)
    
    # Loop through gradients, y-intercepts
    for a in [-7, 0, 2.5, 6]:
        for b in [-4, 0, 1.5]:
            linear_func: Callable = lambda x, a=a, b=b: a*x + b

            # Loop through integral limits
            for (min, max) in [(0, 2), (2.5, 4), (-4, 1.5)]:
                    exact_integral = exact_integral_linear(a, b, min, max)

                    quadrature_integral = rule.integrate(linear_func, min, max)
                    assert isclose(quadrature_integral, exact_integral)


def check_cubic_functions(rule: QuadratureRule):
    """
    Check that the input quadrature rule is exact for a selection of cubic functions
    """
    # Exact integral function
    def exact_integral_cubic(a: float, b: float, c: float, d: float, min: float, max: float) -> float:
        F: Callable = lambda x: (a / 4) * x ** 4 + (b / 3) * x ** 3 + (c / 2) * x ** 2 + d * x
        return F(max) - F(min)

    # Loop through coefficients
    for a in [-10, 0, 1.5, 3]:
        for b in [-5, 0, 2.5]:
            for c in [-1, 0, 4.5, 7]:
                for d in [-5, 0, 1.5]:
                    cubic_func: Callable = lambda x, a=a, b=b, c=c, d=d: a * x ** 3 + b * x ** 2 + c * x + d

                    # Loop through integral limits
                    for (min, max) in [(0, 1), (1.5, 5), (-3, 2.5)]:
                            exact_integral = exact_integral_cubic(a, b, c, d, min, max)

                            quadrature_integral = rule.integrate(cubic_func, min, max)
                            assert isclose(quadrature_integral, exact_integral)


def check_quintic_functions(rule: QuadratureRule):
    """
    Check that the input quadrature rule is exact for a selection of quintic functions
    """
    # Exact integral function
    def exact_integral_quintic(a: float, b: float, c: float, d: float, e: float, f: float, min: float, max: float) -> float:
        F: Callable = lambda x: (a / 6) * x ** 6 + (b / 5) * x ** 5 + (c / 4) * x ** 4 + (d / 3) * x ** 3 + (e / 2) * x ** 2 + f * x
        return F(max) - F(min)

    # Loop through coefficients
    for a in [-10, 0, 1.5, 3]:
        for b in [-5, 0, 2.5]:
            for c in [-1, 0, 4.5, 7]:
                for d in [-5, 0, 1.5]:
                    for e in [-6, 0, 1.5, 8]:
                         for f in [-2.5, 0, 1, 5.5]:
                            quintic_func: Callable = lambda x, a=a, b=b, c=c, d=d: a * x ** 5 + b * x ** 4 + c * x ** 3 + d * x ** 2 + e * x + f

                            # Loop through integral limits
                            for (min, max) in [(0, 1), (1.5, 5), (-3, 2.5)]:
                                    exact_integral = exact_integral_quintic(a, b, c, d, e, f, min, max)

                                    quadrature_integral = rule.integrate(quintic_func, min, max)
                                    assert isclose(quadrature_integral, exact_integral)
