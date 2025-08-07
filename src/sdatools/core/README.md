# `sdatools.core`

This module contains fundamental utilities and mathematical functions used throughout the `sdatools` package. 

The `functions` sub-module currently implements: 
- $\phi(x)$, the probability density function (PDF) of the Normal distribution
- $\Phi(x)$, the cumulative distribution function (CDF) of the Normal Distribution
- `erf(x)`, the error function (used in the calculation of the CDF for the Normal distribution). 

The `utils` sub-module presents a decorator, `vectorise_input`, which allows the above functions (and others) to handle what is defined as `NumericLike` types in the `types` sub-module: scalar values (`int` or `float`), `np.ndarray`, `pd.Series`, and `pd.DataFrame`.