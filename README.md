# SDATools: Statistics & Data Analysis Tools
**Author:** Mike Fuller
**Last Updated:** 20th June 2025

This repository contains the source code for **SDATools**, a Python package I created to reinforce my understanding of various statistics and data analysis tools, whilst getting hands-on with Python to build a functioning package that myself and others can use to carry out statistical tests and data analysis.

SDATools has the following structure:
```bash
├───src
│   └───sdatools
│       ├───distributions
│       │   ├───continuous
│       │   ├───discrete
│       ├───functions
│       ├───numerical_methods
│       └───statistics
└───tests
```

The `distributions` directory contains a `distribution.py` file, which has an abstract distributions class `Distributions` from which all distributions are built. Furthermore, `distributions/continuous` and `distributions/discrete` contain `continuous_distribution.py` and `discrete_distribution.py` respectively, which have abstract classes `ContinuousDistribution` for continuous distributions and `DiscreteDistribution` for discrete distributions. I implemented these abstract classes so that probabilty density and mass functions (PDFs/PMFs) and cumulative distribution functions (CDFs) are enforced when new distributions are added.

The `functions` directory contains Python files for non-standard functions that are desirable to have throughout the SDATools package. As of version 0.1.0, this directory only contains `erf.py`, a numerical approximation of the error function `erf(x)` (for use in the calculation of the CDF for the Normal distribution),

The `numerical_methods` directory will contain algorithms and approximation techniques that will be desirable across the SDATools package. As of version 0.1.0, this directory contains `quadrature.py`, which contains a range of Newton-Cotes qudarature rules (Trapezium, Simpson, Simpson 3/8, Boole) and has been abstracted with the `QuadratureRule` base class for ease of future quadrature rule additions, and `interpolator.py`, which is a work-in-progress but will similarly contain interpolation techniques, abstracted by an `Interpolant` base class.

Finally, the `statistics` directory - not properly started in v0.1.0 - will contain statistical techniques and tests that an end user can leverage for research / data analysis purposes. Currently, the directory only includes an early-stages version of a summary statistics file, `summary_statistics.py`.

As I add more functionality to the SDATools package, I am also producing unit tests in the `tests` directory to check that the package's components are behaving as expected.