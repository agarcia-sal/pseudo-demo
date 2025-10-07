from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ordered_values = sorted(array_of_integers)
    smallest_number = min(array_of_integers)

    smallest_pos = 0
    while smallest_pos < len(array_of_integers):
        if array_of_integers[smallest_pos] == smallest_number:
            break
        smallest_pos += 1

    shifted_sequence: List[int] = []
    total_elements = len(array_of_integers)

    iter_pos = smallest_pos
    while iter_pos < total_elements:
        shifted_sequence.append(array_of_integers[iter_pos])
        iter_pos += 1

    iter_pos = 0
    while iter_pos < smallest_pos:
        shifted_sequence.append(array_of_integers[iter_pos])
        iter_pos += 1

    counter = 0
    while counter < total_elements:
        if shifted_sequence[counter] != ordered_values[counter]:
            return False
        counter += 1

    return True