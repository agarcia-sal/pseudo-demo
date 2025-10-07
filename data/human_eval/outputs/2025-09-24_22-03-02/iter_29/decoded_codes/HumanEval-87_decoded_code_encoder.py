from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords = sorted(coords, key=lambda coord: coord[1], reverse=True)
    coords = sorted(coords, key=lambda coord: coord[0])
    return coords