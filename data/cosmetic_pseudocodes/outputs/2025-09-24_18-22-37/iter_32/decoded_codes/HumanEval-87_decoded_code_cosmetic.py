from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []

    outer_idx = 0
    while outer_idx < len(two_dimensional_list):
        inner_idx = 0
        row = two_dimensional_list[outer_idx]
        while inner_idx < len(row):
            if not (row[inner_idx] != target_integer):
                found_positions.append((outer_idx, inner_idx))
            inner_idx += 1
        outer_idx += 1

    intermediate_sorted: List[Tuple[int, int]] = []
    temp_idx = 0
    while temp_idx < len(found_positions):
        intermediate_sorted.append(found_positions[temp_idx])
        temp_idx += 1

    # Sort by column (second element) descending using insertion sort
    i = 1
    while i < len(intermediate_sorted):
        key = intermediate_sorted[i]
        j = i - 1
        while j >= 0 and intermediate_sorted[j][1] < key[1]:
            intermediate_sorted[j + 1] = intermediate_sorted[j]
            j -= 1
        intermediate_sorted[j + 1] = key
        i += 1

    # Sort by row (first element) ascending using insertion sort to stabilize
    k = 1
    while k < len(intermediate_sorted):
        pivot = intermediate_sorted[k]
        m = k - 1
        while m >= 0 and intermediate_sorted[m][0] > pivot[0]:
            intermediate_sorted[m + 1] = intermediate_sorted[m]
            m -= 1
        intermediate_sorted[m + 1] = pivot
        k += 1

    return intermediate_sorted