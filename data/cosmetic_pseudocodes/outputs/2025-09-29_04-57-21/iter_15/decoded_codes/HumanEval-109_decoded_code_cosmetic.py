from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ordered_sequence = sorted(array_of_integers)
    smallest_element = ordered_sequence[0]
    starting_position = array_of_integers.index(smallest_element)

    rearranged_list = array_of_integers[starting_position:] + array_of_integers[:starting_position]

    for current_index in range(len(array_of_integers)):
        if rearranged_list[current_index] != ordered_sequence[current_index]:
            return False

    return True