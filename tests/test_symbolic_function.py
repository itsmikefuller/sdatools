from sympy import symbols

from sdatools.core.symbolic_function import SymbolicFunction


def test_symbolic_function_creation():
    """Test the creation of a symbolic function."""
    x = symbols('x')
    f = SymbolicFunction(x**2 + 3*x + 2)
    assert f.expr == x**2 + 3*x + 2
    assert f.symbols == [x]


def test_symbolic_function_evaluation():
    """Test the evaluation of a symbolic function."""
    x = symbols('x')
    f = SymbolicFunction(x**2 + 3*x + 2)
    result = f(x=2)
    expected_result = 2**2 + 3*2 + 2
    assert result == expected_result


def test_symbolic_function_addition():
    """Test the addition of two symbolic functions."""
    x = symbols('x')
    f1 = SymbolicFunction(x**2)
    f2 = SymbolicFunction(3*x + 1)
    f_sum = f1 + f2
    expected_expr = x**2 + 3*x + 1
    assert f_sum.expr == expected_expr


def test_symbolic_univariate_derivative():
    """Test the derivative of a univariate function."""
    x = symbols('x')
    f = SymbolicFunction(x**2)
    expected_dfdx = 2 * x 
    dfdx = f.derivative('x')
    assert dfdx == expected_dfdx 
    

def test_symbolic_multivariate_derivative():
    """Test the derivative of a multivariate function."""
    x, y = symbols('x y')
    f = SymbolicFunction(x**2 + 3*y)
    expected_dfdx = 2 * x
    expected_dfdy = 3
    dfdx = f.derivative('x')
    dfdy = f.derivative('y')
    assert dfdx == expected_dfdx
    assert dfdy == expected_dfdy
