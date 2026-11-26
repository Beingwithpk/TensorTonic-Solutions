from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean_val=float(np.mean(x))
    median_val=float(np.median(x))
    values,counts=np.unique(x,return_counts=True)
    mode_val=float(values[np.argmax(counts)])
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val
    }
    pass