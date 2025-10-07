from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    outer = 0
    while outer < len(matrix):
        inner = 0
        while inner < len(matrix[outer]):
            if not (matrix[outer][inner] != key):  # equivalent to matrix[outer][inner] == key
                result.append((outer, inner))
            inner += 1
        outer += 1
    # Sort by column descending, then by row ascending
    result.sort(key=lambda x: x[0])       # sort by row ascending
    result.sort(key=lambda x: x[1], reverse=True)  # then by column descending
    return result