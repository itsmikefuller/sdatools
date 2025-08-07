# `sdatools.numerical_methods`

This module provides a suite of numerical methods for computationally solving a range of problems. It is split into several sub-modules: `interpolation`, `matrix_factorisation`, `optimisation`, `quadrature`, and `root_finding`.

The `quadrature` module contains classes for:

- Trapezium Rule, `TrapeziumRule`
- Simpson's Rule, `SimpsonRule`
- Simpson's 3/8 Rule, `Simpson38Rule`
- Boole's Rule, `BooleRule`

Composite quadrature can also be applied to any above rule using `CompositeRule(rule, num_subintervals)`.

## Structure

All quadrature rules inherit from the abstract base class `QuadratureRule`. The base class forces an `integrate` method to be implemented for each quadrature rule, as well as the following properties:

- `order`: the order of the polynomial interpolant used to derive the quadrature rule
- `exact_order`: the maximum order of polynomials for which the quadrature rule is exact 

## Examples

### Estimating the integral of a polynomial using the Boole Rule

```python
from sdatools.numerical_methods.quadrature import BooleRule
from math import isclose

# Example function to integrate
f: Callable = lambda x: x**4 + 2*x + 1

# Define integration limits
a = 0.0
b = 1.0

# Calculate the exact integral for comparison
exact_integral = (b**5 / 5 + b**2 + b) - (a**5 / 5 + a**2 + a) # 2.2

# Create Boole rule instance
boole_rule = BooleRule()

# Perform integration
integral_boole = boole_rule.integrate(f, a, b)

# Print results
print(f"Integral value with Boole Rule = {integral_boole}") # 2.2
print(f"Error in Composite Boole Rule: {abs(integral_boole - exact_integral)}") # 0.0

# Check results are close to the exact integral
assert isclose(integral_boole, exact_integral), "Composite Boole Rule failed"
```