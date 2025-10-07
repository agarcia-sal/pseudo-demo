from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    idx_outer: int = 0
    collected_coords: List[Tuple[int, int]] = []

    while idx_outer < len(two_dimensional_list):
        idx_inner: int = 0
        while idx_inner < len(two_dimensional_list[idx_outer]):
            if two_dimensional_list[idx_outer][idx_inner] == target_integer:
                collected_coords.append((idx_outer, idx_inner))
            idx_inner += 1
        idx_outer += 1

    sorted_by_first: List[Tuple[int, int]] = []
    sorted_by_second: List[Tuple[int, int]] = []

    for coord_idx1 in range(len(collected_coords)):
        sorted_by_first.append(collected_coords[coord_idx1])

    for coord_idx2 in range(len(collected_coords)):
        sorted_by_second.append(collected_coords[coord_idx2])

    # Selection sort variant on sorted_by_second by second element descending
    n: int = len(sorted_by_second)
    m: int = 0
    while m < n - 1:
        max_pos: int = m
        p: int = m + 1
        while p < n:
            if sorted_by_second[p][1] > sorted_by_second[max_pos][1]:
                max_pos = p
            p += 1
        if max_pos != m:
            sorted_by_second[m], sorted_by_second[max_pos] = sorted_by_second[max_pos], sorted_by_second[m]
        m += 1

    # Insertion sort variant on sorted_by_first by first element ascending
    len_first: int = len(sorted_by_first)
    i: int = 1
    while i < len_first:
        key: Tuple[int, int] = sorted_by_first[i]
        j: int = i - 1
        while j >= 0 and sorted_by_first[j][0] > key[0]:
            sorted_by_first[j + 1] = sorted_by_first[j]
            j -= 1
        sorted_by_first[j + 1] = key
        i += 1

    return sorted_by_first