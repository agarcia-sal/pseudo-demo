from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    i: int = 0
    while i < len(matrix):
        j: int = 0
        while j < len(matrix[i]):
            if not (matrix[i][j] != key):
                positions.append((i, j))
            j += 1
        i += 1

    # Sort by column descending, then by row ascending
    positions.sort(key=lambda x: x[1], reverse=True)
    positions.sort(key=lambda x: x[0])
    return positions