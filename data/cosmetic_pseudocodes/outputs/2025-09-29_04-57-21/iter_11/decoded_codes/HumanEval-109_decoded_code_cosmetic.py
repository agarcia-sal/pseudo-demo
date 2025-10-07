from typing import List


def move_one_ball(list_of_numbers: List[int]) -> bool:
    if not list_of_numbers:
        return True

    ordered_list = sorted(list_of_numbers)
    smallest_element = list_of_numbers[0]
    position = 0

    while position < len(list_of_numbers) and list_of_numbers[position] != smallest_element:
        position += 1

    rearranged_list = list_of_numbers[position:] + list_of_numbers[:position]

    for counter in range(len(list_of_numbers)):
        if rearranged_list[counter] != ordered_list[counter]:
            return False

    return True