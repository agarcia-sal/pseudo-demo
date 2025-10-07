from typing import List

def solve(integer_N: int) -> str:
    def sum_digits(list_chars: List[str], idx: int, accumulator: int) -> int:
        if idx == len(list_chars):
            return accumulator
        return sum_digits(list_chars, idx + 1, accumulator + (ord(list_chars[idx]) - ord('0')))

    digit_chars = list(str(integer_N))
    total_sum = sum_digits(digit_chars, 0, 0)
    binary_str = bin(total_sum)[3:]
    return binary_str