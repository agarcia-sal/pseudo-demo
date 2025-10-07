from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    pos_list: List[Tuple[int, int]] = []
    outer_counter: int = 0
    while outer_counter < len(two_dimensional_list):
        inner_counter: int = 0
        while inner_counter < len(two_dimensional_list[outer_counter]):
            if two_dimensional_list[outer_counter][inner_counter] == target_integer:
                temp_pair = (outer_counter, inner_counter)
                pos_list.append(temp_pair)
            inner_counter += 1
        outer_counter += 1

    # Sort by second element descending, then by first element ascending (stable sort)
    pos_list.sort(key=lambda x: x[1], reverse=True)
    pos_list.sort(key=lambda x: x[0])
    return pos_list