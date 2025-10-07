from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ordered_list = sorted(array_of_integers)
    smallest_number = min(array_of_integers)
    position_of_smallest = array_of_integers.index(smallest_number)

    shifted_list = array_of_integers[position_of_smallest:] + array_of_integers[:position_of_smallest]

    for idx in range(len(array_of_integers)):
        if shifted_list[idx] != ordered_list[idx]:
            return False

    return True