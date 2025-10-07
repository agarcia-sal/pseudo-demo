from typing import List

def solve(n: int) -> str:
    total: int = 0
    digits_array: List[str] = list(str(n))
    index: int = 0
    while index < len(digits_array):
        total += int(digits_array[index])
        index += 1
    binary_str: str = bin(total)
    return binary_str[2:]