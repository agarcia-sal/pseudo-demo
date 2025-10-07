from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    coordinates: List[Tuple[int, int]] = []
    for row in range(len(two_dimensional_list)):
        for col in range(len(two_dimensional_list[row])):
            if two_dimensional_list[row][col] == target_integer:
                coordinates.append((row, col))
    coordinates.sort(key=lambda x: (x[0], -x[1]))  # Sort by row ascending, col descending
    return coordinates