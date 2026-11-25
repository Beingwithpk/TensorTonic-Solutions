import numpy as np
from numpy.linalg import norm

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    if norm(a)==0 or norm(b)==0:
        return 0.0
    result= float(np.dot(a,b)/(norm(a)*norm(b)))
    return result
    pass