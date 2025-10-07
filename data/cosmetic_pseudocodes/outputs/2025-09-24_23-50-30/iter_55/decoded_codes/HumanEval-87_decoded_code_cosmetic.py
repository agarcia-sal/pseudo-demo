from typing import List, Tuple

def get_row(a_matrix: List[List[int]], a_value: int) -> List[Tuple[int, int]]:
    def traverse_rows(r_idx: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if r_idx == len(a_matrix):
            return acc
        else:
            return traverse_rows(r_idx + 1, collect_columns(a_matrix[r_idx], r_idx, 0, acc))

    def collect_columns(row_data: List[int], r_idx_inner: int, c_idx: int, acc_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if c_idx == len(row_data):
            return acc_inner
        elif row_data[c_idx] == a_value:
            return collect_columns(row_data, r_idx_inner, c_idx + 1, acc_inner + [(r_idx_inner, c_idx)])
        else:
            return collect_columns(row_data, r_idx_inner, c_idx + 1, acc_inner)

    unsorted_coords = traverse_rows(0, [])

    def sorter_first_then_second(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        def sort_by_first(lst_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            return sorted(lst_inner, key=lambda x: x[0])

        def sort_by_second(lst_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            return sorted(lst_inner, key=lambda x: x[1], reverse=True)

        return sort_by_first(sort_by_second(lst))

    return sorter_first_then_second(unsorted_coords)