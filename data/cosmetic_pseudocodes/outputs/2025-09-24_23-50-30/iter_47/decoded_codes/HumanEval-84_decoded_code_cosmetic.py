from typing import List

def solve(integer_N: int) -> str:
    aggregated_sum: int = 0
    digit_str_list: List[str] = list(str(integer_N))
    idx_counter: int = 0
    while idx_counter < len(digit_str_list):
        aggregated_sum += ord(digit_str_list[idx_counter]) - ord('0')
        idx_counter += 1

    complete_binary: str = bin(aggregated_sum)
    binary_trimmed: str = complete_binary[2:]
    return binary_trimmed