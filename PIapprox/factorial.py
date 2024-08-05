import numpy as np

def factorial(n):
    """
    Compute the factorial of n.
    """
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer")
        return np.prod(range(1, n+1))
    except Exception as e:
        print(f"An error occurred while computing factorial: {e}")
        return None