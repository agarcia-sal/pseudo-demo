from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], value: Any) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    outer_index: int = 0
    while outer_index <= len(matrix) - 1:
        inner_index: int = 0
        while inner_index <= len(matrix[outer_index]) - 1:
            if matrix[outer_index][inner_index] == value:
                result.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1
    # Sort by inner index descending, then by outer index ascending
    result.sort(key=lambda x: x[1], reverse=True)
    result.sort(key=lambda x: x[0])
    return result