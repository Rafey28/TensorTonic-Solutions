import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = [p if X == 1 else (1 - p) for X in x]
    pmf = np.array(pmf)
    mean = float(p)
    variance = float(p *(1 - p))
    return {"pmf": pmf, "mean": mean, "variance": variance}
    pass