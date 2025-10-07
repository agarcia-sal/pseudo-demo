from typing import List, Tuple

def get_row(matrix: List[List[int]], val: int) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    ridx = 0
    while ridx < len(matrix):
        cidx = 0
        while cidx < len(matrix[ridx]):
            if matrix[ridx][cidx] == val:
                positions.append((ridx, cidx))
            cidx += 1
        ridx += 1
    # Sort by row ascending; if rows equal, by col descending
    positions.sort(key=lambda a: (a[0], -a[1]))
    return positions