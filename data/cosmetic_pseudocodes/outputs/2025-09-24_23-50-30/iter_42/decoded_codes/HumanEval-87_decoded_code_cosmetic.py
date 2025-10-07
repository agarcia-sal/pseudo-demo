from typing import List, Tuple

def get_row(input_matrix: List[List[int]], query_number: int) -> List[Tuple[int, int]]:

    result_positions: List[Tuple[int, int]] = []
    outer_idx = 0
    while outer_idx < len(input_matrix):
        inner_idx = 0
        while inner_idx < len(input_matrix[outer_idx]):
            if not (input_matrix[outer_idx][inner_idx] != query_number):
                result_positions.append((outer_idx, inner_idx))
            inner_idx += 1
        outer_idx += 1

    def sort_by_column_desc(list_to_sort: List[Tuple[int, int]], accumulator: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not list_to_sort:
            return accumulator
        pivot = list_to_sort[0]
        rest = list_to_sort[1:]
        greater: List[Tuple[int, int]] = []
        lesser_equal: List[Tuple[int, int]] = []
        for item in rest:
            if item[1] > pivot[1]:
                greater.append(item)
            else:
                lesser_equal.append(item)
        return sort_by_column_desc(greater, []) + [pivot] + sort_by_column_desc(lesser_equal, []) + accumulator

    after_col_sort = sort_by_column_desc(result_positions, [])

    def sort_by_row_asc(positions: List[Tuple[int, int]], acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not positions:
            return acc
        pivot = positions[0]
        remaining = positions[1:]
        smaller_equal: List[Tuple[int, int]] = []
        bigger: List[Tuple[int, int]] = []
        for element in remaining:
            if element[0] <= pivot[0]:
                smaller_equal.append(element)
            else:
                bigger.append(element)
        return sort_by_row_asc(smaller_equal, []) + [pivot] + sort_by_row_asc(bigger, []) + acc

    fully_sorted = sort_by_row_asc(after_col_sort, [])
    return fully_sorted