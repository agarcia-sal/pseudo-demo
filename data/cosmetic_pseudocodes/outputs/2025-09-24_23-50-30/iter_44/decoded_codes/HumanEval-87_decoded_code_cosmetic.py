from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    def traverse_rows(rIndex: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if rIndex >= len(matrix):
            return acc

        def traverse_columns(cIndex: int, rowAcc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if cIndex >= len(matrix[rIndex]):
                return rowAcc
            elif matrix[rIndex][cIndex] != key:
                return traverse_columns(cIndex + 1, rowAcc)
            else:
                return traverse_columns(cIndex + 1, rowAcc + [(rIndex, cIndex)])

        return traverse_rows(rIndex + 1, acc + traverse_columns(0, []))

    found_positions = traverse_rows(0, [])
    sorted_by_col_desc = sorted(found_positions, key=lambda pos: pos[1], reverse=True)
    result = sorted(sorted_by_col_desc, key=lambda pos: pos[0])
    return result