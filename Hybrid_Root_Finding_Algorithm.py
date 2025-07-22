import numpy as np

def Hybrid_Function(f, bounds=None, fp=None, x0=None, iterations=100, tol=1.0e-8):
    """
    A hybrid function combining bisection, regula-falsi, and Newton-Raphson methods to find a root of f.
    The function adapts between methods based on performance and convergence behaviour.

    Parameters:
    f: Function for which the root is being found.
    bounds: Tuple of two numbers for the initial search interval.
    fp: Derivative of f.
    x0: Initial value for Newton-Raphson method.
    iterations: Maximum number of iterations.

    Returns:
    - Approximation of the root, or None if no root is found.
    - Iterations depending on which method is used.
    """
    if fp is None:
        def fp(x, h=1e-5):
            try:
                return (f(x + h) - f(x - h))/(2*h)
            except:
                return None

    if x0 is not None and fp is not None:  # Newton-Raphson Method, which will run if x0 and fp are provided
        newton_iterations = 0
        for i in range(iterations):
            newton_iterations += 1
            if abs(fp(x0)) < tol:  # Avoid division by zero
                break
            x1 = x0 - f(x0) / fp(x0)
            if abs(x1 - x0) < tol:
                return x1, newton_iterations
            x0 = x1

    if bounds is not None:  # Bisection and Regula-Falsi methods require bounds to be defined
        lower, upper = bounds

        # Start with Regula-Falsi, then switch to Newton-Raphson if conditions improve
        regula_iterations = 0
        while abs(f(lower)) > tol and abs(f(upper)) > tol:
            regula_iterations += 1
            root = (lower * f(upper) - upper * f(lower)) / (f(upper) - f(lower))
            if f(root) * f(lower) < 0:
                upper = root
            else:
                lower = root
            if abs(f(root)) < tol:
                return root, regula_iterations

            # Switch to Newton-Raphson if Regula-Falsi is not converging fast enough
            if regula_iterations >= 5 and fp is not None:  # Threshold for switching
                if abs(f(root)) > tol:
                    x0 = root
                    newton2_iterations = 0
                    for i in range(iterations):
                        newton2_iterations += 1
                        if abs(fp(x0)) < tol:  # Avoid division by zero
                            break
                        x1 = x0 - f(x0) / fp(x0)
                        if abs(x1 - x0) < tol:
                            return x1, regula_iterations + newton2_iterations
                        x0 = x1
                    break  # break out of Regula-Falsi loop

        # Bisection Method if Regula-Falsi isn't suitable
        bisection_iterations = 0
        while upper - lower > tol:
            bisection_iterations += 1
            midpoint = (lower + upper) / 2
            if f(lower) * f(midpoint) < 0:
                lower, upper = lower, midpoint
            else:
                lower, upper = midpoint, upper

            if abs(f(midpoint)) < tol:
                return midpoint, bisection_iterations

    print("No roots found within the tolerance.")
    return None, 0
