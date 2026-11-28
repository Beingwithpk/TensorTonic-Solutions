import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    n=len(x)
    sum=0
    for i in range(n):
        sum+=x[i]*p[i]
    return sum
    pass