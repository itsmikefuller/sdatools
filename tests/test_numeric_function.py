from sdatools.core.numeric_function import NumericFunction
import math


def test_univariate_derivative():
    """Test the derivative of a univariate function."""
    f = NumericFunction(lambda x: x**2)
    x0 = 3.0
    expected_derivative = 2 * x0 
    df = f.derivative(var_index=0, h=1e-5, x=x0)
    assert math.isclose(df, expected_derivative, rel_tol=1e-5)
    

def test_multivariate_derivative():
    """Test the derivative of a multivariate function."""
    f = NumericFunction(lambda x, y: x**2 + 3*y)
    x0, y0 = 2.0, 1.0
    expected_dfdx = 2 * x0
    expected_dfdy = 3
    dfdx = f.derivative(var_index=0, h=1e-5, x=x0, y=y0)
    dfdy = f.derivative(var_index=1, h=1e-5, x=x0, y=y0)
    assert math.isclose(dfdx, expected_dfdx, rel_tol=1e-5)
    assert math.isclose(dfdy, expected_dfdy, rel_tol=1e-5)
