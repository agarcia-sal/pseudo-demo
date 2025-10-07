from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    accumulator: List[Tuple[int, int]] = []

    def iterate_rows(row_idx: int) -> None:
        if row_idx >= len(two_dimensional_list):
            return

        def iterate_columns(col_idx: int) -> None:
            if col_idx >= len(two_dimensional_list[row_idx]):
                return
            # condition NOT(two_dimensional_list[row_idx][col_idx] != target_integer) means equality
            if two_dimensional_list[row_idx][col_idx] == target_integer:
                accumulator.append((row_idx, col_idx))
            iterate_columns(col_idx + 1)

        iterate_columns(0)
        iterate_rows(row_idx + 1)

    iterate_rows(0)

    # Sort by row ascending
    accumulator.sort(key=lambda x: x[0])
    # Sort by column descending within same row
    accumulator.sort(key=lambda x: (x[0], -x[1]))

    return accumulator