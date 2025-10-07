from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    accum: List[Tuple[int, int]] = []
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if not (matrix[i][j] != key):
                accum.append((i, j))
            j += 1
        i += 1
    # sort by second element descending, then by first element ascending
    accum.sort(key=lambda x: (-x[1], x[0]))
    # then sort by first element ascending in a stable way
    accum.sort(key=lambda x: x[0])
    return accum