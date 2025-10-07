from typing import List, Tuple

def get_row(input_matrix: List[List[int]], query_value: int) -> List[Tuple[int, int]]:
    position_stack: List[Tuple[int, int]] = []

    def explore_rows(row_idx: int) -> None:
        if row_idx >= len(input_matrix):
            return

        def inspect_columns(col_idx: int) -> None:
            if col_idx >= len(input_matrix[row_idx]):
                return
            if input_matrix[row_idx][col_idx] == query_value:
                position_stack.append((row_idx, col_idx))
            inspect_columns(col_idx + 1)

        inspect_columns(0)
        explore_rows(row_idx + 1)

    explore_rows(0)

    # Sort by column ascending (second element of pair)
    position_stack.sort(key=lambda pair: pair[1])
    # Then sort by row descending (first element of pair)
    position_stack.sort(key=lambda pair: pair[0], reverse=True)

    return position_stack