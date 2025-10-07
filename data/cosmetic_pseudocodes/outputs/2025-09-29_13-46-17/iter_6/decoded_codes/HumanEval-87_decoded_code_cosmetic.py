from typing import List, Tuple, Callable


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    # Recursively collect coordinates where elements match target_integer
    def helper(accumulated_coords: List[Tuple[int, int]], r_idx: int) -> List[Tuple[int, int]]:
        if not (r_idx < len(two_dimensional_list)):
            return accumulated_coords

        def inner_loop(c_idx: int, coords_accum: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if not (c_idx < len(two_dimensional_list[r_idx])):
                return coords_accum
            condition_check = two_dimensional_list[r_idx][c_idx] == target_integer
            updated_coords = coords_accum + [(r_idx, c_idx)] if condition_check else coords_accum
            return inner_loop(c_idx + 1, updated_coords)

        return helper(inner_loop(0, accumulated_coords), r_idx + 1)

    collected_coords = helper([], 0)

    def sort_by_col_desc(coords: List[Tuple[int, int]], i: int, j: int) -> bool:
        return coords[i][1] >= coords[j][1]

    def sort_by_row_asc(coords: List[Tuple[int, int]], i: int, j: int) -> bool:
        return coords[i][0] <= coords[j][0]

    def bubble_sort(coords: List[Tuple[int, int]], comp_func: Callable[[List[Tuple[int, int]], int, int], bool]) -> List[Tuple[int, int]]:
        length = len(coords)

        def loop_outer(i: int, coords_arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if not (i < length - 1):
                return coords_arr

            def loop_inner(j: int, arr_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if not (j < length - i - 1):
                    return arr_inner
                need_swap = not comp_func(arr_inner, j, j + 1)
                if need_swap:
                    arr_inner = arr_inner[:]  # copy to avoid mutating input list outside this scope
                    arr_inner[j], arr_inner[j + 1] = arr_inner[j + 1], arr_inner[j]
                else:
                    # no swap needed, keep arr_inner as is
                    pass
                return loop_inner(j + 1, arr_inner)

            return loop_outer(i + 1, loop_inner(0, coords_arr))

        return loop_outer(0, coords)

    after_col_sort = bubble_sort(collected_coords, sort_by_col_desc)
    after_row_sort = bubble_sort(after_col_sort, sort_by_row_asc)

    return after_row_sort