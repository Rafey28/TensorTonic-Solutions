import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x = np.array(x, dtype=float)
    gamma = np.array(gamma, dtype=float)
    beta = np.array(beta, dtype=float)
    
    dims = len(x.shape)
    if dims == 2:
        axes = 0 
    else:
        axes = (0,2,3)
        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)

    mean_ = np.mean(x, axis = axes, keepdims=True)
    variance = np.var(x,axis = axes, keepdims = True)
    normalized = (x - mean_) / np.sqrt(variance + eps)
    y = gamma * normalized + beta
    
    return y
    
    pass