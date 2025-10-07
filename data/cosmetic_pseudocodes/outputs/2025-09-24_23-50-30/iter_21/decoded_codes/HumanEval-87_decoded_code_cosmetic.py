from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index = 0
    while outer_index < len(two_dimensional_list):
        inner_index = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            if not (two_dimensional_list[outer_index][inner_index] != target_integer):
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    def sort_by_second_desc_then_first_asc(
        list_to_sort: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        # Sort primarily by first element ascending, then by second element descending
        return sorted(list_to_sort, key=lambda a: (a[0], -a[1]))

    found_positions = sort_by_second_desc_then_first_asc(found_positions)
    return found_positions