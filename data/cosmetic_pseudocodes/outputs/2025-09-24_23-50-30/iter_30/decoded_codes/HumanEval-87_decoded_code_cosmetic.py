from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    result_positions: List[Tuple[int, int]] = []
    outer_idx = 0
    while outer_idx < len(matrix):
        inner_idx = 0
        while inner_idx < len(matrix[outer_idx]):
            if matrix[outer_idx][inner_idx] == key:
                result_positions.append((outer_idx, inner_idx))
            inner_idx += 1
        outer_idx += 1

    # Sort by column descending
    result_positions.sort(key=lambda x: x[1], reverse=True)
    # Sort by row ascending (stable sort preserves previous order)
    result_positions.sort(key=lambda x: x[0])
    return result_positions