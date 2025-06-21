from sdatools.functions.function import Function
import math


def test_univariate_derivative():
    """Test the derivative of a univariate function."""
    f = Function(lambda x: x**2, name="f")
    x0 = 3.0
    expected_derivative = 2 * x0 
    df = f.derivative(var_index=0, h=1e-5, x=x0)
    assert math.isclose(df, expected_derivative, rel_tol=1e-5)
    assert str(df) == "Function: f_derivative()"

def test_multivariate_derivative():
    """Test the derivative of a multivariate function."""
    f = Function(lambda x, y: x**2 + 3*y, name="f")
    x0, y0 = 2.0, 1.0
    expected_dfdx = 2 * x0
    expected_dfdy = 3
    dfdx = f.derivative(var_index=0, h=1e-5, x=x0, y=y0)
    dfdy = f.derivative(var_index=1, h=1e-5, x=x0, y=y0)
    assert math.isclose(dfdx, expected_dfdx, rel_tol=1e-5)
    assert math.isclose(dfdy, expected_dfdy, rel_tol=1e-5)
    assert str(dfdx) == "Function: f_derivative(0)()"
    assert str(dfdy) == "Function: f_derivative(1)()"
