# Abstract quadrature rule

from .abstract.quadrature_rule import QuadratureRule

# Quadrature rules

from .rules.trapezium import TrapeziumRule
from .rules.simpson import SimpsonRule, Simpson38Rule
from .rules.boole import BooleRule
from .rules.composite import CompositeRule

# Quadrature engine

from .quadrature_engine import QuadratureEngine


__all__ = [
    "QuadratureRule",
    "TrapeziumRule",
    "SimpsonRule",
    "Simpson38Rule",
    "BooleRule",
    "CompositeRule",
    "QuadratureEngine"
]
