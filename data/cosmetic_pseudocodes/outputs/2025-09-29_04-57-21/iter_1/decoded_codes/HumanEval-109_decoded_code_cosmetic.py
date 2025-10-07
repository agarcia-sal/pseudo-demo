from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    sorted_version = sorted(array_of_integers)
    smallest_element = array_of_integers[0]
    pos_of_smallest = 0
    for i in range(1, len(array_of_integers)):
        if array_of_integers[i] < smallest_element:
            smallest_element = array_of_integers[i]
            pos_of_smallest = i

    rearranged_array = array_of_integers[pos_of_smallest:] + array_of_integers[:pos_of_smallest]

    for j in range(len(array_of_integers)):
        if rearranged_array[j] != sorted_version[j]:
            return False
    return True