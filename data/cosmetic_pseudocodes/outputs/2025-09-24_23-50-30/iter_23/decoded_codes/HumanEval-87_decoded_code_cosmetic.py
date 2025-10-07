from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    results: List[Tuple[int, int]] = []
    for idx_row in range(len(matrix)):
        for idx_col in range(len(matrix[idx_row])):
            if matrix[idx_row][idx_col] == key:
                results.insert(0, (idx_row, idx_col))  # prepend (idx_row, idx_col) to results
    # Sort by column descending
    results.sort(key=lambda x: x[1], reverse=True)
    # Then sort by row ascending (stable sort)
    results.sort(key=lambda x: x[0])
    return results