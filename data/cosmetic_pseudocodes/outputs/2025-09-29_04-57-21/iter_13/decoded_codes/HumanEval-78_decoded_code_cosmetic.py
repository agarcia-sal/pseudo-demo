from typing import Callable

def hex_key(string_num: str) -> int:
    prime_hex_chars: tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    prime_digit_count: int = 0

    def check_char(position: int) -> None:
        nonlocal prime_digit_count
        if position == len(string_num):
            return
        if string_num[position] in prime_hex_chars:
            prime_digit_count += 1
        check_char(position + 1)

    check_char(0)
    return prime_digit_count