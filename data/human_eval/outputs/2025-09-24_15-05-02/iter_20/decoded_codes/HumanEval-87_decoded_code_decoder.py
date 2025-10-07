from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    # Sort by second element (column) descending, then by first element (row) ascending
    coords.sort(key=lambda t: t[1], reverse=True)
    coords.sort(key=lambda t: t[0])
    return coords