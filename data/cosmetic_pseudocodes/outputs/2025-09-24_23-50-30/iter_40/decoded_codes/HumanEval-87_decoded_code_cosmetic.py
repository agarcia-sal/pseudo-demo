from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    result_set: List[Tuple[int, int]] = []
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if not (matrix[i][j] != key):
                result_set.append((i, j))
            j += 1
        i += 1
    # Sort by column descending, then by row ascending
    result_set.sort(key=lambda x: x[1], reverse=True)
    result_set.sort(key=lambda x: x[0])
    return result_set