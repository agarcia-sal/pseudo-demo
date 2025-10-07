from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def find_matches_by_indices(i: int, j: int, accum: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if i >= len(two_dimensional_list):
            return accum
        elif j >= len(two_dimensional_list[i]):
            return find_matches_by_indices(i + 1, 0, accum)
        else:
            if two_dimensional_list[i][j] == target_integer:
                accum.append((i, j))
            return find_matches_by_indices(i, j + 1, accum)

    matched_coords: List[Tuple[int, int]] = find_matches_by_indices(0, 0, [])

    def sort_by_column_descending(list_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return sorted(list_coords, key=lambda x: x[1], reverse=True)

    def sort_by_row_ascending(list_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        return sorted(list_coords, key=lambda x: x[0])

    step_one = sort_by_column_descending(matched_coords)
    step_two = sort_by_row_ascending(step_one)
    return step_two