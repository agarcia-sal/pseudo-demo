from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    tally_map: dict[int, int] = {}
    for current_num in list_of_numbers:
        tally_map[current_num] = tally_map.get(current_num, 0) + 1

    for current_num in list_of_numbers:
        freq_val = tally_map[current_num]
        if freq_val > 2:
            return False

    sorted_flag = True
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            sorted_flag = False
            break

    return sorted_flag