from typing import List

def move_one_ball(input_list: List[int]) -> bool:
    if not input_list:
        return True

    ordered_list = sorted(input_list)
    smallest_element = min(input_list)
    pivot_position = input_list.index(smallest_element)

    shifted_list = input_list[pivot_position:] + input_list[:pivot_position]

    for i in range(len(input_list)):
        if shifted_list[i] != ordered_list[i]:
            return False

    return True