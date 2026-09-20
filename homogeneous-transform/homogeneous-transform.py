import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    T = np.asarray(T)
    points = np.asarray(points)
    
    # Check if input is a single 1D point (shape: (3,))
    single_point = (points.ndim == 1)
    if single_point:
        points = points.reshape(1, 3)
        
    points_homog = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed_homog = points_homog @ T.T
  
    result = transformed_homog[:, :-1]
    
    if single_point:
        return result[0]
        
    return result