from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coords.append((i, j))
    # Sort by second element descending
    coords.sort(key=lambda coord: coord[1], reverse=True)
    # Then sort by first element ascending (stable sort)
    coords.sort(key=lambda coord: coord[0])
    return coords