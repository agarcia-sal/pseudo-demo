from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    while True:
        if not (len(array_of_integers) > 0):
            return True
        break

    ascending_version = sorted(array_of_integers)
    smallest_element = array_of_integers[0]
    pos_of_smallest = 0
    i = 1
    while i < len(array_of_integers):
        if array_of_integers[i] < smallest_element:
            smallest_element = array_of_integers[i]
            pos_of_smallest = i
        i += 1

    shifted_list: List[int] = []
    j = pos_of_smallest
    while j < len(array_of_integers):
        shifted_list.append(array_of_integers[j])
        j += 1
    k = 0
    while k < pos_of_smallest:
        shifted_list.append(array_of_integers[k])
        k += 1

    counter = 0
    while counter < len(array_of_integers):
        if shifted_list[counter] != ascending_version[counter]:
            return False
        counter += 1

    return True