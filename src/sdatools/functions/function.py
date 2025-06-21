from typing import Callable


class Function:
    """
    A class to represent a mathematical function with various operations and properties.
    It supports addition, subtraction, multiplication, division, power operations,
    and numerical derivatives using finite difference.

    Example:
        f = Function(lambda x, y: x**2 + 3*y)
        value = f(2, 1)  # evaluates f(2, 1)
        dfdx = f.derivative(var_index=0, 2, 1)
        dfdy = f.derivative(var_index=1, 2, 1)

    Attributes:
        func (callable): The function to be represented.
        name (str): The name of the function.

    Methods:
        __call__(self, *args, **kwargs): Call the function with the given arguments.
        __repr__(self): Return a string representation of the function.
        __str__(self): Return a string representation of the function.
        __eq__(self, other): Check if two functions are equal by comparing their names.
        __hash__(self): Return a hash based on the function's name.
        __add__(self, other): Add two functions together.
        __sub__(self, other): Subtract one function from another.
        __mul__(self, other): Multiply two functions together.
        __rmul__(self, other): Right-multiply a function by another.
        __truediv__(self, other): Divide one function by another.
        __pow__(self, power): Raise a function to a power.
        derivative(self, var_index=0, h=1e-5, *args, **kwargs): Calculate the derivative of the function using finite differences.
    
    """
    def __init__(self, func: Callable, name=None):
        self.func = func
        self.name = name or func.__name__
    
    def __call__(self, *args, **kwargs):
        """Call the function with the given arguments."""
        return self.func(*args, **kwargs)
    
    def __repr__(self):
        """Return a string representation of the function."""
        return f"Function(name={self.name})"
    
    def __str__(self):
        """Return a string representation of the function."""
        return f"Function: {self.name}()"
    
    def __eq__(self, other):
        """Check if two functions are equal by comparing their names."""
        if isinstance(other, Function):
            return self.name == other.name
        return False
    
    def __hash__(self):
        """Return a hash based on the function's name."""
        return hash(self.name)
    
    def __add__(self, other):
        """Add two functions together."""
        if isinstance(other, Function):
            return Function(lambda x: self.func(x) + other.func(x), name=f"{self.name} + {other.name}")
        raise TypeError("Can only add Function instances.")
    
    def __sub__(self, other):
        """Subtract one function from another."""
        if isinstance(other, Function):
            return Function(lambda x: self.func(x) - other.func(x), name=f"{self.name} - {other.name}")
        raise TypeError("Can only subtract Function instances.")
    
    def __mul__(self, other):
        """Multiply two functions together."""
        if isinstance(other, Function):
            return Function(lambda x: self.func(x) * other.func(x), name=f"{self.name} * {other.name}")
        raise TypeError("Can only multiply Function instances.")
    
    def __rmul__(self, other):
        """Right-multiply a function by another."""
        if isinstance(other, Function):
            return Function(lambda x: other.func(x) * self.func(x), name=f"{other.name} * {self.name}")
        raise TypeError("Can only multiply Function instances.")
    
    def __truediv__(self, other):
        """Divide one function by another."""
        if isinstance(other, Function):
            return Function(lambda x: self.func(x) / other.func(x), name=f"{self.name} / {other.name}")
        raise TypeError("Can only divide Function instances.")
    
    def __pow__(self, power):
        """Raise a function to a power."""
        if isinstance(power, (int, float)):
            return Function(lambda x: self.func(x) ** power, name=f"{self.name} ** {power}")
        raise TypeError("Power must be an integer or float.")
    
    def derivative(self, var_index=0, h=1e-5, *args, **kwargs):
        """
        Compute the numerical derivative with respect to variable at var_index,
        using centered finite differences.

        Parameters:
            var_index (int): index of variable to differentiate
            h (float): step size
            *args: function arguments
            **kwargs: keyword arguments to function

        Returns:
            float: approximate derivative
        """
        args = list(args)
        if var_index < 0 or var_index >= len(args):
            raise IndexError("Variable index out of range.")
        # Create a copy of args to modify
        args = args.copy()
        original_value = args[var_index]
        # Calculate the derivative using central difference
        args[var_index] = original_value + h
        f_plus = self.func(*args, **kwargs)
        args[var_index] = original_value - h
        f_minus = self.func(*args, **kwargs)
        args[var_index] = original_value
        return (f_plus - f_minus) / (2 * h)
    