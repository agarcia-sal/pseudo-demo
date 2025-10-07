from typing import List


def move_one_ball(numbers_list: List[int]) -> bool:
    if not numbers_list:
        return True

    ordered_list = sorted(numbers_list)

    smallest_number = numbers_list[0]
    smallest_pos = 0
    for pos_counter, num in enumerate(numbers_list):
        if num < smallest_number:
            smallest_number = num
            smallest_pos = pos_counter

    rearranged_list = []
    current_pos = smallest_pos
    length = len(numbers_list)
    for _ in range(length):
        rearranged_list.append(numbers_list[current_pos])
        current_pos = (current_pos + 1) % length

    for pointer in range(length):
        if rearranged_list[pointer] != ordered_list[pointer]:
            return False

    return True