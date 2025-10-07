from typing import List


def solve(integer_N: int) -> str:
    accumulator: int = 0
    digits_list: List[str] = list(str(integer_N))
    for index in range(1, len(digits_list)):
        current_char: str = digits_list[index]
        digit_value: int = ord(current_char) - ord('0')
        accumulator += digit_value
    binary_equiv: str = bin(accumulator)
    result_string: str = binary_equiv[3:]
    return result_string