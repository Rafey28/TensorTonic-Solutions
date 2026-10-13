import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    # Write code here
    values, index, counts = np.unique(y_train, return_index=True, return_counts=True)
    max_count = np.max(counts)
    tie_positions = np.where(counts == max_count)[0]
    best_tie_index = tie_positions[np.argmin(index[tie_positions])]
    
    majority_class = values[best_tie_index]
    return np.repeat(majority_class, len(X_test))
    pass