from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    matched_positions: List[Tuple[int, int]] = []
    outer_counter: int = 0
    while outer_counter < len(two_dimensional_list):
        inner_counter: int = 0
        while inner_counter < len(two_dimensional_list[outer_counter]):
            if not (two_dimensional_list[outer_counter][inner_counter] != target_integer):
                matched_positions.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    # Sort by column descending, then by row ascending
    matched_positions.sort(key=lambda item: item[1], reverse=True)
    matched_positions.sort(key=lambda item: item[0])
    return matched_positions