from sys import float_info
from math import log


# Largest safe exponent before float overflows, ~709.782712893384
EXP_LIMIT: float = log(float_info.max)
