# Support Vector Machines (SVMs)

**Last Updated:** 2nd August 2025

## Introduction: Linear SVMs

Consider a binary classification problem: that is, samples $(\underline{x}^{(i)},y^{(i)})$ of observations $\underline{x}^{(i)}\in \mathbb{R}^n$ and targets $y^{(i)} \in \{Y, N\}$ are provided, and a classifier function $f$ is sought such that input observations $\underline{x}'$ outside the sample dataset can be appropriately classified (as $Y$ or $N$) via $f(\underline{x}')$.

For a simple example, let's consider a 2D problem where the observations are clearly separable by a straight line:

<p align="center">
  <img src="images/fig_1.png" />
</p>

The problem can be re-written as finding the parameters $w, b \in \mathbb{R}$ such that the line $y=wx+b$ best separates the two groups of observations. In higher dimensions, we want to find a hyperplane 

$$H=\{\underline{x}\in\mathbb{R}^n : \underline{w}^T\underline{x}+\underline{b}=0\}$$

that does this.

The line $y=\frac{1}{3}x$ could separate the classes of red and blue observations, for example:

<p align="center">
  <img src="images/fig_2.png" />
</p>

If we re-write classes as $y^{(i)}\in \{-1,1\}$, with $1$ representing the blue class and $-1$ representing the red class, then the function 
$$f(x)=\text{sgn}(wx+b)$$
correctly classifies the observations. The "best" classifier $y=wx+b$ would then be the line that gives rise to the maximum margin between the line and the observations, i.e. the geometric distance $d=\frac{|w\underline{x}^{(i)}+b|}{||w||}$.