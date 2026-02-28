import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    m, n = X.shape  
    w = np.zeros(n)
    b = 0.0

    for i in range(steps):
        z = np.dot(X, w) + b
        
        prediction = _sigmoid(z)
        
    
        #clip the prediction to avoid log(0) which results in NaN
        prediction = np.clip(prediction, 1e-15, 1 - 1e-15)
        cost = -np.mean(y * np.log(prediction) + (1 - y) * np.log(1 - prediction))

    
        error = prediction - y
        dw_dj = (1 / m) * np.dot(X.T, error)
        
        db_dj = (1 / m) * np.sum(error)

        #Implement gradient descent
        w = w - lr * dw_dj
        b = b - lr * db_dj
        
    return w, b
    
    pass