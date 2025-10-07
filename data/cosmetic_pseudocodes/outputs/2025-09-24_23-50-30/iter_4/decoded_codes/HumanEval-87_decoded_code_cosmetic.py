from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def find_positions(current_row: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if current_row >= len(two_dimensional_list):
            return acc

        def scan_columns(col: int, acc_col: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if col >= len(two_dimensional_list[current_row]):
                return acc_col
            acc_col_new = (
                acc_col + [(current_row, col)]
                if two_dimensional_list[current_row][col] == target_integer
                else acc_col
            )
            return scan_columns(col + 1, acc_col_new)

        updated_acc = acc + scan_columns(0, [])
        return find_positions(current_row + 1, updated_acc)

    matches = find_positions(0, [])

    matches_sorted_first = sorted(matches, key=lambda x: x[0])
    matches_sorted = sorted(matches_sorted_first, key=lambda x: x[1], reverse=True)

    return matches_sorted