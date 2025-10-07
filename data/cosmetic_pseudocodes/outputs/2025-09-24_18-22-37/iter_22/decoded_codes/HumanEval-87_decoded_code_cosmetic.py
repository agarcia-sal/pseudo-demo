from typing import List, Tuple

def get_row(matrix: List[List[int]], number: int) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    i = 0
    while i <= len(matrix) - 1:
        j = 0
        while j <= len(matrix[i]) - 1:
            if not (matrix[i][j] != number):
                points.append((i, j))
            j += 1
        i += 1
    # Sort first by column descending, then by row ascending
    temp_list = sorted(points, key=lambda element: element[1], reverse=True)
    points = sorted(temp_list, key=lambda element: element[0])
    return points