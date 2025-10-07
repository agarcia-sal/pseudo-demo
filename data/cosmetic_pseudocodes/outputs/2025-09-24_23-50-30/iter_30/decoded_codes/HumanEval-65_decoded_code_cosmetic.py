from typing import List


def circular_shift(integer_rho: int, integer_delta: int) -> str:
    list_chars: List[str] = list(str(integer_rho))
    length_n: int = len(list_chars)
    if not (integer_delta <= length_n):
        return "".join(reversed(list_chars))
    split_index: int = length_n - integer_delta
    part_A: List[str] = list_chars[split_index:length_n]
    part_B: List[str] = list_chars[0:split_index]
    combined: List[str] = part_A + part_B
    return "".join(combined)