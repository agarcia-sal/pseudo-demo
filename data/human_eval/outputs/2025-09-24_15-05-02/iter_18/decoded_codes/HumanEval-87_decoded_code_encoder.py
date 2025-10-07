from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                coords.append((i, j))
    # Sort by second element descending, then by first element ascending
    coords.sort(key=lambda coord: coord[1], reverse=True)
    coords.sort(key=lambda coord: coord[0])
    return coords