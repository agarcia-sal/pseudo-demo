from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    return sorted(coords, key=lambda c: (-c[1], c[0]))