from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    outer_index = 0

    while outer_index < len(two_dimensional_list):
        inner_index = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            if not (two_dimensional_list[outer_index][inner_index] != target_integer):
                positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    # Sort primarily by row ascending (a[0] < b[0]), secondarily by column ascending (a[1] < b[1])
    sorted_by_column = sorted(positions, key=lambda a: a[1])
    sorted_by_row = sorted(sorted_by_column, key=lambda a: a[0])

    return sorted_by_row