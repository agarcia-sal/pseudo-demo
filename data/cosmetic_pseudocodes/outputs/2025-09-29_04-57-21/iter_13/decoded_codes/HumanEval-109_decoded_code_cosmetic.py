from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ascending_ordered_list = sorted(array_of_integers)
    smallest_value = min(array_of_integers)

    pivot_position = array_of_integers.index(smallest_value)

    reordered_sequence = array_of_integers[pivot_position:] + array_of_integers[:pivot_position]

    def verify_match(position: int) -> bool:
        if position == len(array_of_integers):
            return True
        if reordered_sequence[position] != ascending_ordered_list[position]:
            return False
        return verify_match(position + 1)

    return verify_match(0)