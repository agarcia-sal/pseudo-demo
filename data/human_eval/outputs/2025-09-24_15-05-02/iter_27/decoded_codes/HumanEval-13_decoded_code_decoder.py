from typing import Union

def greatest_common_divisor(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both a and b must be integers.")
    # Handle case when both inputs are zero (GCD undefined)
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined.")
    # Use absolute values to handle negative inputs
    a_abs, b_abs = abs(a), abs(b)
    while b_abs != 0:
        a_abs, b_abs = b_abs, a_abs % b_abs
    return a_abs