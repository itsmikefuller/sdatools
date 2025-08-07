from sdatools.numerical_methods.quadrature import *

from typing import Callable


class QuadratureEngine:
    """
    Class for choosing and applying a quadrature rule
    """
    def __init__(self):
        # List of available quadrature rules
        self.rules = {
            'trapezium': TrapeziumRule(),
            'simpson': SimpsonRule(),
            'simpson38': Simpson38Rule(),
            'boole': BooleRule()
        }

    # TODO: implement QuadratureEngine functionality
    def integrate(self, f: Callable, a: float, b: float) -> float:
        # Determine if exact integration is possible without composite rule
        
        # Choose composite rule number of subintervals based on the function and interval
        
        # Run simple analysis or trial integrations
        results = {}
        for rule_name, rule in self.rules.items():
            results[rule_name] = rule.integrate(f, a, b)
        
        # Choose the best rule based on some criteria, e.g. speed, accuracy
        
        # Delegate the call to the chosen rule's integrate method

        raise NotImplementedError("Integration logic not implemented. Choose a specific rule or implement the logic.")
