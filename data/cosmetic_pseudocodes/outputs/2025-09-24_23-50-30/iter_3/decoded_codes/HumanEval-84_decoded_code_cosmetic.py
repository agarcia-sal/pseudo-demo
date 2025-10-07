from typing import List


def solve(integer_N: int) -> str:
    sum_accumulator: int = 0
    digits_list: List[str] = list(str(integer_N))
    index: int = 0
    while index < len(digits_list):
        sum_accumulator += int(digits_list[index])
        index += 1
    binary_str_with_prefix: str = bin(sum_accumulator)
    binary_output: str = binary_str_with_prefix[3:]
    return binary_output