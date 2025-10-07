from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    row_index: int = 0
    max_row_index: int = len(two_dimensional_list) - 1

    while row_index <= max_row_index:
        col_index: int = len(two_dimensional_list[row_index]) - 1
        while col_index >= 0:
            curr_value: int = two_dimensional_list[row_index][col_index]
            if curr_value == target_integer:
                result.append((row_index, col_index))
            col_index -= 1
        row_index += 1

    # Sort primarily by column descending, then by row ascending
    result.sort(key=lambda q: (-q[1], q[0]))
    # Then sort by row ascending (this ensures stable final sorting primarily by row asc, secondary by column desc)
    result.sort(key=lambda q: q[0])
    return result