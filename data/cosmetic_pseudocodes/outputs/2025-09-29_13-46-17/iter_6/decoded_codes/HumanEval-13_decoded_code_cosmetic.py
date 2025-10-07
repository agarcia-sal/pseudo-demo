from typing import Callable

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    def inner_gcd(x_value: int, y_value: int) -> int:
        return x_value if y_value == 0 else inner_gcd(y_value, x_value % y_value)

    return inner_gcd(integer_a, integer_b)