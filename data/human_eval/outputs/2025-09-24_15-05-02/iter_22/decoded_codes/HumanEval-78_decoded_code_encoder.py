from typing import Tuple

def hex_key(hexadecimal_string: str) -> int:
    prime_hex_digits: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    prime_digit_count: int = 0
    for index in range(len(hexadecimal_string)):
        if hexadecimal_string[index] in prime_hex_digits:
            prime_digit_count += 1
    return prime_digit_count