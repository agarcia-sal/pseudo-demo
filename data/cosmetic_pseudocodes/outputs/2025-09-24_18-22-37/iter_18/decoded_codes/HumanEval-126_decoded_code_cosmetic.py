from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    map_counter: dict[int, int] = {elem: 0 for elem in list_of_numbers}
    for elem in list_of_numbers:
        map_counter[elem] += 1

    flag_duplicate = False
    for key_element in list_of_numbers:
        if map_counter[key_element] > 2:
            flag_duplicate = True
            break
    if flag_duplicate:
        return False

    position_index = 1
    while position_index <= len(list_of_numbers) - 1:
        if not (list_of_numbers[position_index - 1] <= list_of_numbers[position_index]):
            return False
        position_index += 1
    return True