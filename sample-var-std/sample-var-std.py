import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean_x=np.mean(x)
    n=len(x)
    sum=0
    for i in x:
        sum+=(i-mean_x)**2
    variance=float(sum/(n-1))
    sd=variance**0.5
    return {
        "variance": variance,
        "standard_deviation": sd
    }
    pass