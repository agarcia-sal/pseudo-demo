from typing import List


def solve(integer_N: int) -> str:
    total: int = 0
    digit_list: List[str] = list(str(integer_N))
    for index in range(len(digit_list)):
        total += int(digit_list[index])
    binary_str: str = bin(total)
    trimmed_binary: str = binary_str[3:-1]  # slice from the 4th char to second last
    return trimmed_binary