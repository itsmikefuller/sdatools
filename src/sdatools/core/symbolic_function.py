from sympy import Expr, lambdify, symbols, Symbol, Add, Mul
from typing import Union

from sdatools.core.base_function import Function


class SymbolicFunction(Function):
    """A class for symbolic functions that can compute derivatives."""

    def __init__(self, expr: Expr):
        """Initialize with a function."""
        self.expr = expr
        # Extract symbols from the expression
        self.symbols = sorted(expr.free_symbols, key=lambda s: str(s))
        # Create a callable function from the expression 
        self._numeric = lambdify(self.symbols, expr, modules='numpy')

    def __call__(self, **kwargs):
        """Call the function with the given arguments."""
        values = [kwargs[str(s)] for s in self.symbols]
        return self._numeric(*values)
        
    def __add__(self, other: Union['SymbolicFunction', Expr]) -> 'SymbolicFunction':
        """Add two functions together."""
        if isinstance(other, SymbolicFunction):
            return SymbolicFunction(Add(self.expr, other.expr))
        elif isinstance(other, Expr):
            return SymbolicFunction(Add(self.expr, other))
        raise TypeError("Can only add SymbolicFunction instances.")
    
    def __sub__(self, other: Union['SymbolicFunction', Expr]) -> 'SymbolicFunction':
        """Subtract one function from another."""
        if isinstance(other, SymbolicFunction):
            return SymbolicFunction(Add(self.expr, -other.expr))
        elif isinstance(other, Expr):
            return SymbolicFunction(Add(self.expr, -other))
        raise TypeError("Can only subtract SymbolicFunction instances.")
    
    def __mul__(self, other: Union['SymbolicFunction', Expr]) -> 'SymbolicFunction':
        """Multiply two functions together."""
        if isinstance(other, SymbolicFunction):
            return SymbolicFunction(Mul(self.expr, other.expr))
        elif isinstance(other, Expr):
            return SymbolicFunction(Mul(self.expr, other))
        raise TypeError("Can only multiply SymbolicFunction instances.")
    
    def __rmul__(self, other: Union['SymbolicFunction', Expr]) -> 'SymbolicFunction':
        """Right-multiply a function by another."""
        if isinstance(other, SymbolicFunction):
            return SymbolicFunction(Mul(other.expr, self.expr))
        elif isinstance(other, Expr):
            return SymbolicFunction(Mul(other, self.expr))
        raise TypeError("Can only right-multiply SymbolicFunction instances.")
    
    def __truediv__(self, other: Union['SymbolicFunction', Expr]) -> 'SymbolicFunction':
        """Divide one function by another."""
        if isinstance(other, SymbolicFunction):
            return SymbolicFunction(Mul(self.expr, other.expr**-1))
        elif isinstance(other, Expr):
            return SymbolicFunction(Mul(self.expr, other**-1))
        raise TypeError("Can only divide SymbolicFunction instances.")
    
    def __pow__(self, power):
        """Raise a function to a power."""
        if isinstance(power, (int, float)):
            return SymbolicFunction(self.expr ** power)
        raise TypeError("Power must be an integer or float.")
    
    def derivative(self, symbol: Union[str, Symbol]) -> 'SymbolicFunction':
        """
        Compute the derivative of the function with respect to a variable.
        
        Example:
            from sympy import symbols
            x, y = symbols('x y')
            f = SymbolicFunction(x**2 + 3*y)
            df_dx = f.derivative('x')
            print(df_dx)
            2*x
            df_dy = f.derivative('y')
            print(df_dx(x=2, y=1))
            4.0
        """
        if isinstance(symbol, str):
            symbol = symbols(symbol)
        if symbol not in self.symbols:
            raise ValueError(f"Symbol {symbol} not found in function.")
        derivative_expr = self.expr.diff(symbol)
        return SymbolicFunction(derivative_expr)
    
    def integrate(self, *args, **kwargs):
        """Integrate the function symbolically."""
        from sympy import integrate
        integral_expr = integrate(self.expr, *args, **kwargs)
        if not isinstance(integral_expr, Expr):
            raise TypeError(f"Cannot wrap object of type {type(integral_expr)} as SymbolicFunction.")
        return SymbolicFunction(integral_expr)
