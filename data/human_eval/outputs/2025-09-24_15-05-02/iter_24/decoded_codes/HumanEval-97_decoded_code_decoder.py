from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> int:
    last_digit_a = abs(int(a)) % 10
    last_digit_b = abs(int(b)) % 10
    return last_digit_a * last_digit_b