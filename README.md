<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="logo.png">
  <img alt="sdatools Logo" src="logo.png">
</picture>

-----------------

# sdatools: Statistics & Data Analysis Tools

**Author:** Mike Fuller

**Last Updated:** 4th August 2025

This repository contains the source code for `sdatools`, a **work-in-progress** Python package I am developing to kill two birds with one stone: build my very first Python package whilst refreshing my knowledge of various statistics and data analysis techniques. I am taking a bottom-up approach as much as possible: whilst the package occasionally leverages well-known scientific packages like `numpy`, `pandas`, and `scikit-learn`, I aim to build most modules from scratch.

## Contents

- [Key Features](#key-features)
- [Tests & Case Studies](#tests--case-studies)
- [Source Code Layout](#source-code-layout)
- [Ongoing Development](#ongoing-development)

## Key Features

### `sdatools.core`

Contains abstract base classes for functions, symbolic functions, and numeric functions. I leverage the Python package [`sympy`](https://www.sympy.org/en/index.html) to implement symbolic functions and computational algebra in `symbolic_function.py`. 

The `functions` sub-module will contain Python files for non-standard functions that are desirable to have throughout `sdatools`. As of version 0.1.0, `erf.py` has been implemented, which contains a numerical approximation of the error function `erf(x)` (for use in the calculation of the CDF for the Normal distribution).

The vision is to allow functions in `sdatools` to be treated as symbolic for as long as possible, until defaulting to a numeric function, so that various computations can be made quicker by using an exact solution.

### [`sdatools.data_visualisation`](https://github.com/itsmikefuller/sdatools/tree/main/src/sdatools/data_visualisation)

Will contain a selection of data visualisation classes for eventual use in a model validation dashboard, for example. Q-Q plots have been partially implemented. Further visualisations to be implemented include:
- Biplots
- Box plots
- Dendrograms
- Histograms
- Pairs plots
- P-P plots
- Scree plots

### [`sdatools.distributions`](https://github.com/itsmikefuller/sdatools/tree/main/src/sdatools/distributions)

Contains a suite of continuous and discrete distributions. The `base_distribution.py` file contains an abstract base class, `Distribution`, from which all distributions are built. This class is further built upon in the `continuous` and `discrete` sub-modules, which have abstract classes `ContinuousDistribution` and `DiscreteDistribution` respectively. The purpose of these abstract classes is to make sure that probabilty density functions (PDFs), probability mass functions (PMFs), and cumulative distribution functions (CDFs) are enforced whenever new distributions are added to `sdatools`.

### [`sdatools.numerical_methods`](https://github.com/itsmikefuller/sdatools/tree/main/src/sdatools/numerical_methods)

Will contain algorithms and approximation techniques that will be desirable across the `sdatools` package. As of version 0.1.0, the `quadrature` sub-module has been populated with a range of Newton-Cotes qudarature rules (Trapezium, Simpson, Simpson 3/8, Boole), and has been abstracted with the `QuadratureRule` base class for ease of future quadrature rule additions.

### [`sdatools.parameter_estimation`](https://github.com/itsmikefuller/sdatools/tree/main/src/sdatools/parameter_estimation)

Will contain techniques for estimating distribution parameters from a dataset and assessing the accuracy of the parameters, such as maximum likelihood estimation (MLE) and confidence intervals.

### `sdatools.supervised_learning`

This module will contain standard learning techniques for dealing with labelled datasets, such as linear and multivariate regressions, support vector machines (SVMs), and neural networks.

### `sdatools.unsupervised_learning`

Will contain standard techniques for dealing with unlabelled datasets, such as hierarchical and $k$-means clustering, and principal components analysis (PCA). 

The techniques in both supervised and unsupervised learning often seek to ask the following questions:
- How can we visualise the dataset in the most informative way?
- For large datasets, is it possible to reduce the dataset's size (dimension) whilst retaining all (or almost all) information?
- Can we identify distinct subgroups or clusters within the data that reflect its underlying structure?
 
### `sdatools.validation`

Will contain a selection of statistical techniques and tests that an end user can run for model validation purposes. The `goodness_of_fit` sub-module will contain a variety of statistical tests, such as chi-squared, Kolmogorov-Smirnov, Shapiro-Wilk, and Anderson-Darling. The `cross-validation` sub-module will contain a class for running out-of-sample testing.

## Tests & Case Studies

Outside of the source code, this repository has `case_studies` and `tests`. I am regularly producing unit tests in the `tests` directory to check that the package's components are behaving as expected. In due course, I will also add real-world examples of using `sda_tools` to the `case_studies` directory, along with more documentation to this README and throughout the package.

## Source Code Layout

The `sdatools` source code has the following structure:

```bash
└───src
    └───sdatools
        ├───core
        │   └───functions
        ├───data_visualisation
        ├───distributions
        │   ├───continuous
        │   └───discrete
        ├───numerical_methods
        │   ├───interpolation
        │   ├───matrix_factorisation
        │   ├───optimisation
        │   ├───quadrature
        │   └───root_finding
        ├───parameter_estimation
        ├───supervised_learning
        │   ├───decision_tree
        │   ├───k_nearest_neighbours
        │   ├───linear_regression
        │   ├───logistic_regression
        │   ├───neural_network
        │   └───support_vector_machine
        ├───unsupervised_learning
        │   ├───clustering
        │   ├───dimensionality_reduction
        │   └───neural_network
        └───validation
            ├───cross_validation
            └───goodness_of_fit
```

## Ongoing Development

My current focus is building out the `distributions` module, as well as a small selection of goodness-of-fit tests in the `validation` module.