from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def check_positions(curr_pos: int) -> bool:
        if curr_pos == len(array_of_integers):
            return True
        if rotated_seq[curr_pos] == sorted_seq[curr_pos]:
            return check_positions(curr_pos + 1)
        return False

    if not array_of_integers:
        return True

    sorted_seq = sorted(array_of_integers)
    minimum_element = array_of_integers[0]
    found_index = 0
    idx = 1

    while idx < len(array_of_integers):
        if array_of_integers[idx] < minimum_element:
            minimum_element = array_of_integers[idx]
            found_index = idx
        idx += 1

    rotated_seq = array_of_integers[found_index:] + array_of_integers[:found_index]

    return check_positions(0)