from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []

    def explore_column(row_pos: int, col_pos: int, acc_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if col_pos >= len(two_dimensional_list[row_pos]):
            return acc_coords
        updated_coords = acc_coords + [(row_pos, col_pos)] if two_dimensional_list[row_pos][col_pos] == target_integer else acc_coords
        return explore_column(row_pos, col_pos + 1, updated_coords)

    def explore_row(r_pos: int, acc_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if r_pos >= len(two_dimensional_list):
            return acc_coords
        after_columns = explore_column(r_pos, 0, acc_coords)
        return explore_row(r_pos + 1, after_columns)

    coords_unsorted = explore_row(0, coords)

    def swap(xs: List[Tuple[int, int]], i: int, j: int) -> List[Tuple[int, int]]:
        xs[i], xs[j] = xs[j], xs[i]
        return xs

    def sort_desc_sec(xs: List[Tuple[int, int]], i: int, j: int) -> List[Tuple[int, int]]:
        if j >= len(xs):
            return xs
        if i < len(xs):
            if xs[i][1] < xs[j][1]:
                return sort_desc_sec(swap(xs, i, j), i + 1, j)
            return sort_desc_sec(xs, i + 1, j)
        return sort_desc_sec(xs, 0, j + 1)

    def sort_asc_first(xs: List[Tuple[int, int]], k: int, l: int) -> List[Tuple[int, int]]:
        if l >= len(xs):
            return xs
        if k < l:
            if xs[k][0] > xs[l][0]:
                return sort_asc_first(swap(xs, k, l), k + 1, l)
            return sort_asc_first(xs, k + 1, l)
        return sort_asc_first(xs, 0, l + 1)

    coords_after_second_sort = sort_desc_sec(coords_unsorted, 0, 0)
    coords_after_first_sort = sort_asc_first(coords_after_second_sort, 0, 0)

    return coords_after_first_sort