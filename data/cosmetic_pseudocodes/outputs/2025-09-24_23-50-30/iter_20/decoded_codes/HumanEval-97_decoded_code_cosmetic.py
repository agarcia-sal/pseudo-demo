from typing import Union

def multiply(alpha: int, beta: int) -> int:
    omega: int = abs(alpha % 10)
    sigma: int = abs(beta % 10)
    return omega * sigma