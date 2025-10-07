from typing import List, Tuple

def get_row(matrix: List[List[int]], number: int) -> List[Tuple[int, int]]:
    def helper_find_positions(pos_list: List[Tuple[int, int]], r: int, c: int) -> List[Tuple[int, int]]:
        if r == len(matrix):
            return pos_list
        if c == len(matrix[r]):
            return helper_find_positions(pos_list, r + 1, 0)
        if matrix[r][c] != number:
            return helper_find_positions(pos_list, r, c + 1)
        return helper_find_positions(pos_list + [(r, c)], r, c + 1)

    result_positions = helper_find_positions([], 0, 0)

    def sort_by_row_then_col(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        idx = 1
        while idx < len(lst):
            if lst[idx][0] < lst[idx - 1][0]:
                lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
                idx = 1
                continue
            if lst[idx][0] == lst[idx - 1][0]:
                if lst[idx][1] > lst[idx - 1][1]:
                    lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
                    idx = 1
                    continue
            idx += 1
        return lst

    ordered_positions = sort_by_row_then_col(result_positions)

    return ordered_positions