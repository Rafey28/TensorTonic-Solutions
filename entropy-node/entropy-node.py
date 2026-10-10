import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    values, counts = np.unique(y, return_counts = True)
    prob = counts / len(y)
    return -np.dot(prob,np.log2(prob))
    pass