from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    i = 0
    while i < len(lst):
        row = lst[i]
        j = 0
        while j < len(row):
            if row[j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords.sort(key=lambda t: t[1], reverse=True)
    coords.sort(key=lambda t: t[0])
    return coords