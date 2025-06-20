# Debatable whether we need this

class Function:
    def __init__(self, func, name=None):
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
    
    def derivative(self):
        raise NotImplementedError("Derivative method is not implemented. Use a numerical differentiation method or a symbolic library.")
    
    def is_polynomial(self):
        """Check if the function is a polynomial."""
        raise NotImplementedError("is_polynomial method is not implemented. Use a polynomial fitting method or a symbolic library.")
    