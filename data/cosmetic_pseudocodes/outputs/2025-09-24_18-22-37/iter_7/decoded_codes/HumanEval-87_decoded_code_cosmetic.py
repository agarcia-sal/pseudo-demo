from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    position_collection: List[Tuple[int, int]] = []
    outer_counter = 0
    while outer_counter < len(two_dimensional_list):
        inner_counter = 0
        while inner_counter < len(two_dimensional_list[outer_counter]):
            current_element = two_dimensional_list[outer_counter][inner_counter]
            if current_element == target_integer:
                position_collection.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1
    # Sort by column index descending
    position_collection.sort(key=lambda x: x[1], reverse=True)
    # Then stable sort by row index ascending
    position_collection.sort(key=lambda x: x[0])
    return position_collection