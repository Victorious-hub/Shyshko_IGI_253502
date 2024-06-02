from utils import *

"""Task 1: Variant 27. Calculate arcsin(x) function, using function expansion.
Compare with math alternative, using eps
"""

EPS = 1e-10


@timing_average
def custom_asin(x: float | int, eps: float) -> float | int:
    """Calculate the arcsin function using function expansion

    Args:
        x (float | int): number
        eps (float): precision

    Returns:
        float | int: arcsin(x)
    """
    result = 0
    prev_result = 0

    for n in range(500):
        result += custom_factorial(2*n) / (custom_factorial(n) 
                                           ** 2*4**n * (2*n+1)) * x**(2*n+1)
        if abs(result - prev_result) < eps:
            break
        prev_result = result
    
    return (n, result,)