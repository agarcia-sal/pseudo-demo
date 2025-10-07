from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    ordered_version = sorted(array_of_integers)
    smallest_element = float('inf')
    position_of_smallest = 0
    current_position = 0

    while current_position < len(array_of_integers):
        if array_of_integers[current_position] < smallest_element:
            smallest_element = array_of_integers[current_position]
            position_of_smallest = current_position
        current_position += 1

    rearranged: List[int] = []
    total_length = len(array_of_integers)
    cursor = 0

    while cursor < total_length:
        adjusted_index = (position_of_smallest + cursor) % total_length
        rearranged.append(array_of_integers[adjusted_index])
        cursor += 1

    idx = 0
    while idx < total_length:
        if rearranged[idx] != ordered_version[idx]:
            return False
        idx += 1

    return True