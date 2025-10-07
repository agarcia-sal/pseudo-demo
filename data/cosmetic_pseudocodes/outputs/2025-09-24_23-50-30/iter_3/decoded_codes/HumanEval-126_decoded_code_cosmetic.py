from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    tally_map: dict[int, int] = {}
    for num in list_of_numbers:
        tally_map[num] = tally_map.get(num, 0) + 1
    for count in tally_map.values():
        if count > 2:
            return False
    position = 1
    while position < len(list_of_numbers):
        if list_of_numbers[position] < list_of_numbers[position - 1]:
            return False
        position += 1
    return True