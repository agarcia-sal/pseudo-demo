from typing import List


def solve(integer_N: int) -> str:
    total: int = 0
    digits: List[str] = list(str(integer_N))
    for index in range(len(digits)):
        total += int(digits[index])
    binary_str: str = bin(total)
    trimmed_binary: str = binary_str[3:]  # remove '0b' prefix plus one more character
    return trimmed_binary