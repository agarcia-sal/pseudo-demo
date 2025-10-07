from typing import List

def is_sorted(numbers_array: List[int]) -> bool:
    tally_table: dict[int, int] = {}
    idx: int = 0
    n: int = len(numbers_array)
    while idx < n:
        key = numbers_array[idx]
        if key not in tally_table:
            tally_table[key] = 0
        tally_table[key] += 1
        idx += 1

    pos: int = 0
    while pos < n:
        current_val = numbers_array[pos]
        if tally_table[current_val] > 2:
            return False
        pos += 1

    if n <= 1:
        return True

    j: int = 1
    while j < n:
        if numbers_array[j - 1] > numbers_array[j]:
            return False
        j += 1

    return True