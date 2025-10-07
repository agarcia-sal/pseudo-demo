from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ordered_list = sorted(array_of_integers)
    smallest_element = min(array_of_integers)
    position = array_of_integers.index(smallest_element)
    shifted_list = array_of_integers[position:] + array_of_integers[:position]

    pointer = 0
    while pointer < len(array_of_integers):
        if shifted_list[pointer] != ordered_list[pointer]:
            return False
        pointer += 1

    return True