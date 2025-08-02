from abc import ABC, abstractmethod


class Interpolator(ABC):
    """Abstract base class for an interpolator."""
    def __init__(self, x_values: list[float], y_values: list[float]):
        if len(x_values) != len(y_values):
            raise ValueError("x_values and y_values must have the same length.")
        
        self.x_min: float = min(x_values)
        self.x_max: float = max(x_values)
        
        # Sort the x_values and y_values based on x_values ascending order
        sorted_pairs: list[tuple[float, float]] = sorted(zip(x_values, y_values))
        self.x_values: list[float] = [pair[0] for pair in sorted_pairs]
        self.y_values: list[float] = [pair[1] for pair in sorted_pairs]

    @abstractmethod
    def interpolate(self, x: float) -> float:
        pass

    def _check_range(self, x: float):
        """Check if x is within the range of x_values."""
        if not (self.x_min <= x <= self.x_max):
            raise ValueError(f"x={x} is out of bounds for the given x_values: {self.x_min} to {self.x_max}")

    def __call__(self, x: float) -> float:
        self._check_range(x)
        return self.interpolate(x)
    

class LinearInterpolator(Interpolator):
    """Linear interpolation between points."""
    def interpolate(self, x: float) -> float:
        raise NotImplementedError("Linear interpolation is not implemented yet.")


class PolynomialInterpolator(Interpolator):
    """Polynomial interpolation using Lagrange's method."""
    def interpolate(self, x: float) -> float:
        raise NotImplementedError("Polynomial interpolation is not implemented yet.")


class SplineInterpolator(Interpolator):
    """Spline interpolation using cubic splines."""
    def interpolate(self, x: float) -> float:
        raise NotImplementedError("Spline interpolation is not implemented yet.")
    
