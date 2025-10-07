from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    r: int = 0
    while r < len(two_dimensional_list):
        c: int = 0
        while c < len(two_dimensional_list[r]):
            if two_dimensional_list[r][c] == target_integer:
                found_positions.append((r, c))
            c += 1
        r += 1
    # Sort by column descending, then by row ascending
    found_positions.sort(key=lambda x: -x[1])
    found_positions.sort(key=lambda x: x[0])
    return found_positions