# sdatools: Statistics & Data Analysis Tools

**Author:** Mike Fuller

**Last Updated:** 25th June 2025

This repository contains the source code for `sdatools`, a Python package I am developing to refresh my understanding of various statistics and data analysis tools. I am taking a bottom-up approach as much as possible: whilst the package occasionally leverages well-known scientific packages like NumPy, SymPy, and SciPy, most modules will be built from scratch.

# Code Structure

`sdatools` has the following structure:
```bash
├───case_studies
├───src
│   └───sdatools
│       ├───core
│       ├───distributions
│       │   ├───continuous
│       │   ├───discrete
│       ├───functions
│       ├───numerical_methods
│       └───statistics
│           └───goodness_of_fit
└───tests
```

The `core` directory contains WIP abstract base classes for functions, symbolic functions, and numeric functions. I leverage the Python package [SymPy](https://www.sympy.org/en/index.html) to implement symbolic functions and computational algebra in `symbolic_function.py`. The end goal will be to allow functions in `sdatools` to be treated as symbolic for as long as possible, until defaulting to a numeric function, so that various problems can be solved with an exact solution.

The `distributions` directory contains a `distribution.py` file, which has an abstract base class `Distribution` from which all distributions are built. This class is further built upon in `distributions/continuous/continuous_distribution.py` and `distributions/discrete/discrete_distribution.py` respectively, which have abstract classes `ContinuousDistribution` and `DiscreteDistribution`. The purpose of these abstract classes is primarily to make sure that probabilty density and mass functions (PDFs/PMFs) and cumulative distribution functions (CDFs) are enforced when new distributions are added to `sdatools`.

The `functions` directory contains Python files for non-standard functions that are desirable to have throughout `sdatools`. As of version 0.1.0, this directory only contains `erf.py`, a numerical approximation of the error function `erf(x)` (for use in the calculation of the CDF for the Normal distribution),

The `numerical_methods` directory will contain algorithms and approximation techniques that will be desirable across the `sdatools` package. As of version 0.1.0, this directory contains `quadrature.py`, which contains a range of Newton-Cotes qudarature rules (Trapezium, Simpson, Simpson 3/8, Boole) and has been abstracted with the `QuadratureRule` base class for ease of future quadrature rule additions, and `interpolator.py`, which is a work-in-progress but will similarly contain interpolation techniques, abstracted by an `Interpolant` base class.

Finally, the `statistics` directory will contain a selection of statistical techniques and tests that an end user can leverage for research / data analysis purposes. In `statistics/goodness_of_fit`, I have already implemented `QQPlot`, a class for generating Q-Q plots for a given theoretical distribution. I will later build on the `statistics/goodness_of_fit` module by adding various other tests, such as Chi-Squared, Kolmogorov-Smirnov, Shapiro-Wilk, and Anderson-Darling.

Outside of the source code directory, we have `case_studies` and `tests`. I am regularly producing unit tests in the `tests` directory to check that the package's components are behaving as expected. In due course, I will also add real-world examples of using `sda_tools` to the `case_studies` directory, along with more documentation to this README and throughout the package.