from typing import List, Tuple


def get_row(matrix_grid: List[List[str]], search_term: str) -> List[Tuple[int, int]]:
    def accumulate_matches(acc_result: List[Tuple[int, int]], current_row_idx: int) -> List[Tuple[int, int]]:
        if current_row_idx >= len(matrix_grid):
            return acc_result

        def find_in_row(col_idx: int, row_data: List[str], found_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if col_idx >= len(row_data):
                return found_coords
            updated_coords = found_coords
            if row_data[col_idx] == search_term:
                updated_coords = found_coords + [(current_row_idx, col_idx)]
            return find_in_row(col_idx + 1, row_data, updated_coords)

        collected_in_row = find_in_row(0, matrix_grid[current_row_idx], [])
        return accumulate_matches(acc_result + collected_in_row, current_row_idx + 1)

    raw_results = accumulate_matches([], 0)

    def sorting_key_first_asc(coord: Tuple[int, int]) -> int:
        return coord[0]

    def sorting_key_second_desc(coord: Tuple[int, int]) -> int:
        return -coord[1]

    intermediate_sort = sorted(raw_results, key=sorting_key_second_desc)
    final_sort = sorted(intermediate_sort, key=sorting_key_first_asc)

    return final_sort