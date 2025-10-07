from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def scan_columns(row: List[int], col: int = 0, found: List[int] = []) -> List[int]:
        if col == len(row):
            return found
        if row[col] == target_integer:
            found.append(col)
        return scan_columns(row, col + 1, found)

    def scan_rows(matrix: List[List[int]], r: int = 0, accum: List[Tuple[int, int]] = []) -> List[Tuple[int, int]]:
        if r == len(matrix):
            return accum
        matched_cols = scan_columns(matrix[r])
        for c in matched_cols:
            accum.append((r, c))
        return scan_rows(matrix, r + 1, accum)

    position_pairs = scan_rows(two_dimensional_list)

    # Sort first: by first_element ascending, then by second_element descending
    # The pseudocode sorts by row ascending, then by column descending
    # Sorting by row ascending (a[0]) and column descending (a[1]) can be done with:
    # sorted(position_pairs, key=lambda x: (x[0], -x[1]))

    fully_sorted = sorted(position_pairs, key=lambda a: (a[0], -a[1]))
    return fully_sorted