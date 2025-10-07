from typing import List, Tuple, Any

def get_row(lst: List[List[Any]], x: Any) -> List[Tuple[int, int]]:
    coords = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    coords.sort(key=lambda t: t[1], reverse=True)
    coords.sort(key=lambda t: t[0])
    return coords