from typing import List


def solve(integer_N: int) -> str:
    char_list: List[str] = list(str(integer_N))

    def helper(index: int, total: int) -> int:
        if index == len(char_list):
            return total
        return helper(index + 1, total + int(char_list[index]))

    accumulator: int = helper(0, 0)
    binary_str: str = bin(accumulator)  # e.g., '0b1010'
    return binary_str[2:]