from abc import ABC, abstractmethod


class Function(ABC):
    """
    Abstract base class for a function that can be evaluated and differentiated.
    """

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def derivative(self, *args, **kwargs) -> 'Function':
        pass

    @abstractmethod
    def integrate(self, *args, **kwargs) -> 'Function':
        pass

    @abstractmethod
    def __add__(self, other) -> 'Function':
        pass

    @abstractmethod
    def __sub__(self, other) -> 'Function':
        pass

    @abstractmethod
    def __mul__(self, other) -> 'Function':
        pass

    @abstractmethod
    def __rmul__(self, other) -> 'Function':
        pass

    @abstractmethod
    def __truediv__(self, other) -> 'Function':
        pass

    @abstractmethod
    def __pow__(self, power) -> 'Function':
        pass
