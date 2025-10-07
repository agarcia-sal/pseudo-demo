from typing import List

def move_one_ball(input_list: List[int]) -> bool:
    if not input_list:
        return True

    ordered_list = sorted(input_list)
    smallest_element = ordered_list[0]

    pos = 0
    while pos < len(input_list) and input_list[pos] != smallest_element:
        pos += 1

    rearranged = input_list[pos:] + input_list[:pos]

    return all(rearranged[i] == ordered_list[i] for i in range(len(input_list)))