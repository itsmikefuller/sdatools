from sdatools.core.numeric_function import NumericFunction

# TODO: Fix Function derivative() method and update this code accordingly.

def newton_raphson(
    f: NumericFunction,
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> float:
    """
    Find a root of the function f using the Newton-Raphson method.

    Parameters
    ----------
    f : Function
        The function for which to find the root.
    x0 : float
        Initial guess for the root.
    tol : float, optional
        Tolerance for convergence, by default 1e-7.
    max_iter : int, optional
        Maximum number of iterations, by default 100.

    Returns
    -------
    float
        The estimated root of the function.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = f.derivative()(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Maximum number of iterations reached. No solution found."
                     " Consider adjusting the initial guess or function parameters.")
