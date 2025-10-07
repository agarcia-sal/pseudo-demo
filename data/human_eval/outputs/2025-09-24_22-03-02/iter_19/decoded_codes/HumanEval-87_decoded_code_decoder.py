from typing import List, Tuple, TypeVar

T = TypeVar('T')

def get_row(lst: List[List[T]], x: T) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if lst[i][j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords = sorted(coords, key=lambda t: t[1], reverse=True)
    coords = sorted(coords, key=lambda t: t[0])
    return coords