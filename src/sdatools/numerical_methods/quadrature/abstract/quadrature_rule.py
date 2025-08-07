from abc import ABC, abstractmethod
from typing import Callable


class QuadratureRule(ABC):
    """
    Abstract base class for quadrature rules
    """
    @property
    @abstractmethod
    def order(self) -> int:
        """
        The order of the polynomial interpolant used to derive the quadrature rule
        """
        pass

    @property
    @abstractmethod
    def exact_order(self) -> int:
        """
        The maximum order of polynomials for which the quadrature rule is exact 
        """
        pass
    
    @abstractmethod
    def integrate(self, f: Callable, a: float, b: float) -> float:
        pass
