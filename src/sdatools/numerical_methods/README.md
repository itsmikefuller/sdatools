# `sdatools.numerical_methods`

This module provides a suite of numerical methods for computationally solving a range of problems. It is split into several sub-modules: `interpolation`, `matrix_factorisation`, `optimisation`, `quadrature`, and `root_finding`.

Only the `quadrature` sub-module has been started so far. It contains methods for:

- Trapezium Rule
- Simpson's Rule
- Simpson's 3/8 Rule
- Boole's Rule
- Composite quadrature

## Structure

All quadrature rules inherit from the abstract base class `QuadratureRule`, located in `quadrature/quadrature.py`. The base class forces an `integrate` method to be implemented for each quadrature rule.

## Examples

### Estimating the integral of a polynomial using the Boole Rule

```python
from sdatools.numerical_methods.quadrature.quadrature import Quadrature, BooleRule

# Example function to integrate
f: Callable = lambda x: x**4 + 2*x + 1

# Define integration limits
a = 0.0
b = 1.0

# Calculate the exact integral for comparison
exact_integral = (b**5 / 5 + b**2 + b) - (a**5 / 5 + a**2 + a) # 2.2

# Create Boole rule instance
boole_rule = BooleRule()
quadrature_boole = Quadrature(boole_rule)

# Perform integration
integral_boole = quadrature_boole.integrate(f, a, b)

# Print results
print(f"Integral value with Boole Rule = {integral_boole}") # 2.2

# Check results are close to the exact integral
assert abs(integral_boole - exact_integral) < 1e-5, "Composite Boole Rule failed"

# Print error calculation
print(f"Error in Composite Boole Rule: {abs(integral_boole - exact_integral)}") # 0.0
```