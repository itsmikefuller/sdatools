from typing import Callable

from sdatools.numerical_methods.quadrature.quadrature import (
    TrapeziumRule,
    SimpsonRule,
    Simpson38Rule,
    BooleRule,
    CompositeRule,
    Quadrature
)


def test_quadrature_rules():
    """Test various quadrature rules for numerical integration."""
    # Initialise quadrature rules
    trapezium_rule = TrapeziumRule()
    simpson_rule = SimpsonRule()
    simpson38_rule = Simpson38Rule()
    boole_rule = BooleRule()

    # Example function to integrate
    f: Callable = lambda x: x**4 + 2*x + 1
    print("Function to integrate: f(x) = x^4 + 2x + 1")

    # Define integration limits
    a = 0.0
    b = 1.0
    print(f"Integration limits: a = {a}, b = {b}")

    # Calculate the exact integral for comparison
    exact_integral = (b**5 / 5 + b**2 + b) - (a**5 / 5 + a**2 + a)
    print(f"Exact Integral = {exact_integral}")
    print("")

    '''Classic quadrature rules'''
    # Create quadrature instances
    quadrature_trapezium = Quadrature(trapezium_rule)
    quadrature_simpson = Quadrature(simpson_rule)
    quadrature_simpson38 = Quadrature(simpson38_rule)
    quadrature_boole = Quadrature(boole_rule)

    # Perform integration using quadrature rules
    integral_trapezium = quadrature_trapezium.integrate(f, a, b)
    integral_simpson = quadrature_simpson.integrate(f, a, b)
    integral_simpson38 = quadrature_simpson38.integrate(f, a, b)
    integral_boole = quadrature_boole.integrate(f, a, b)

    # Print results
    print(f"Trapezium Rule = {integral_trapezium}")
    print(f"Simpson Rule = {integral_simpson}")
    print(f"Simpson 3/8 Rule = {integral_simpson38}")
    print(f"Boole Rule = {integral_boole}")
    print("")

    # Assert results are close to the exact integral
    assert abs(integral_trapezium - exact_integral) < 1e-5, "Trapezium Rule failed"
    assert abs(integral_simpson - exact_integral) < 1e-5, "Simpson Rule failed"
    assert abs(integral_simpson38 - exact_integral) < 1e-5, "Simpson 3/8 Rule failed"
    assert abs(integral_boole - exact_integral) < 1e-5, "Boole Rule failed"

    # Print error calculations
    print(f"Error in Trapezium Rule: {abs(integral_trapezium - exact_integral)}")
    print(f"Error in Simpson Rule: {abs(integral_simpson - exact_integral)}")
    print(f"Error in Simpson 3/8 Rule: {abs(integral_simpson38 - exact_integral)}")
    print(f"Error in Boole Rule: {abs(integral_boole - exact_integral)}")
    print("")

    '''Composite quadrature rules'''
    # Create composite quadrature instances over 10 subintervals
    composite_trapezium = CompositeRule(trapezium_rule, num_subintervals=10)
    composite_simpson = CompositeRule(simpson_rule, num_subintervals=10)
    composite_simpson38 = CompositeRule(simpson38_rule, num_subintervals=10)
    composite_boole = CompositeRule(boole_rule, num_subintervals=10)
    
    # Perform integration using composite rules
    integral_trapezium = composite_trapezium.integrate(f, a, b)
    integral_simpson = composite_simpson.integrate(f, a, b)
    integral_simpson38 = composite_simpson38.integrate(f, a, b)
    integral_boole = composite_boole.integrate(f, a, b)

    # Print results
    print(f"Composite Trapezium Rule = {integral_trapezium}")
    print(f"Composite Simpson Rule = {integral_simpson}")
    print(f"Composite Simpson 3/8 Rule = {integral_simpson38}")
    print(f"Composite Boole Rule = {integral_boole}")   
    print("")

    # Assert results are close to the exact integral
    assert abs(integral_trapezium - exact_integral) < 1e-5, "Composite Trapezium Rule failed"
    assert abs(integral_simpson - exact_integral) < 1e-5, "Composite Simpson Rule failed"
    assert abs(integral_simpson38 - exact_integral) < 1e-5, "Composite Simpson 3/8 Rule failed"
    assert abs(integral_boole - exact_integral) < 1e-5, "Composite Boole Rule failed"

    # Print error calculations
    print(f"Error in Composite Trapezium Rule: {abs(integral_trapezium - exact_integral)}")
    print(f"Error in Composite Simpson Rule: {abs(integral_simpson - exact_integral)}")
    print(f"Error in Composite Simpson 3/8 Rule: {abs(integral_simpson38 - exact_integral)}")
    print(f"Error in Composite Boole Rule: {abs(integral_boole - exact_integral)}")
