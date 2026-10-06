import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    L = max_len if max_len is not None else max((len(row) for row in seqs), default = 0)
    if not seqs:
        return np.empty((0, L), dtype=int)
    
    result = []
    for row in seqs:
        if len(row) >= L:
            truncated = row[:L]
            result.append(truncated)
        else:
            padded = row + [pad_value] * (L - len(row))
            result.append(padded)
    return np.array(result, dtype = int)
    
    pass