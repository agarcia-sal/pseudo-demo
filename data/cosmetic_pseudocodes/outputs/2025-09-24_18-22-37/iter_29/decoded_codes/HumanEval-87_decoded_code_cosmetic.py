from typing import List, Tuple

def get_row(matrix: List[List[int]], value: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    outer_idx = 0
    while outer_idx < len(matrix):
        inner_idx = 0
        while inner_idx < len(matrix[outer_idx]):
            current_element = matrix[outer_idx][inner_idx]
            if current_element == value:
                entry = (outer_idx, inner_idx)
                result.append(entry)
            inner_idx += 1
        outer_idx += 1

    # Sort descending by column index (inner_idx)
    temp_sorted = sorted(result, key=lambda x: x[1], reverse=True)
    # Then sort ascending by row index (outer_idx)
    final_sorted = sorted(temp_sorted, key=lambda y: y[0])
    return final_sorted