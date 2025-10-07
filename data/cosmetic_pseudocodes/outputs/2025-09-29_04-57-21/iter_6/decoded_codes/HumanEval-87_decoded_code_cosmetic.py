from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    rowCursor = 0
    while rowCursor < len(matrix):
        colPointer = 0
        while colPointer < len(matrix[rowCursor]):
            currentVal = matrix[rowCursor][colPointer]
            if not currentVal != key:
                positions.append((rowCursor, colPointer))
            colPointer += 1
        rowCursor += 1
    # Sort by column descending, then by row ascending
    positions.sort(key=lambda x: -x[1])
    positions.sort(key=lambda x: x[0])
    return positions