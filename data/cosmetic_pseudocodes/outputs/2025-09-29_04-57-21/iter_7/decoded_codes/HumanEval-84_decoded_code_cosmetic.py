from typing import Iterator

def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_iter: Iterator[str] = iter(str(integer_N))
    while True:
        try:
            current_char: str = next(digit_iter)
        except StopIteration:
            break
        numeric_value: int = int(current_char)
        accumulator += numeric_value
    bin_str: str = bin(accumulator)
    result: str = bin_str[2:]
    return result