from typing import List, Tuple


def get_row(array_matrix: List[List[int]], search_value: int) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    outer_counter: int = 0

    while outer_counter < len(array_matrix):
        inner_counter: int = 0
        while inner_counter < len(array_matrix[outer_counter]):
            if array_matrix[outer_counter][inner_counter] == search_value:
                result_positions.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    def sort_by_col_desc(list_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return sorted(list_positions, key=lambda pos: pos[1], reverse=True)

    def sort_by_row_asc_then_col_desc(input_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # Sort by first element ascending, then by second element descending
        return sorted(sort_by_col_desc(input_positions), key=lambda pos: pos[0])

    sorted_positions: List[Tuple[int, int]] = sort_by_row_asc_then_col_desc(result_positions)

    return sorted_positions