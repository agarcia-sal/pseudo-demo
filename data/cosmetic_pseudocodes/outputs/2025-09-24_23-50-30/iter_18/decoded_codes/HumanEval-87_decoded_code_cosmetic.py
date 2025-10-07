from typing import List, Dict, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    matches_dict: Dict[Tuple[int, int], bool] = {}
    outer_index: int = 0
    while outer_index < len(two_dimensional_list):
        current_row: List[int] = two_dimensional_list[outer_index]
        inner_index: int = 0
        while inner_index < len(current_row):
            # Condition: current_row[inner_index] == target_integer
            if current_row[inner_index] == target_integer:
                matches_dict[(outer_index, inner_index)] = True
            inner_index += 1
        outer_index += 1

    pair_list: List[Tuple[int, int]] = []
    for key in matches_dict:
        pair_list.append(key)

    idx_to_second: List[int] = []
    i: int = 0
    while i < len(pair_list):
        idx_to_second.append(pair_list[i][1])
        i += 1

    # Bubble sort pair_list and idx_to_second descending by the second element
    j: int = 0
    while j < len(idx_to_second):
        k: int = 0
        while k < len(idx_to_second) - 1:
            if idx_to_second[k] < idx_to_second[k + 1]:
                idx_to_second[k], idx_to_second[k + 1] = idx_to_second[k + 1], idx_to_second[k]
                pair_list[k], pair_list[k + 1] = pair_list[k + 1], pair_list[k]
            k += 1
        j += 1

    sorted_array: List[Tuple[int, int]] = pair_list

    # Bubble sort sorted_array ascending by the first element of the tuples
    m: int = 0
    while m < len(sorted_array):
        n: int = 0
        while n < len(sorted_array) - 1:
            if sorted_array[n][0] > sorted_array[n + 1][0]:
                sorted_array[n], sorted_array[n + 1] = sorted_array[n + 1], sorted_array[n]
            n += 1
        m += 1

    return sorted_array