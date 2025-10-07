from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: Dict[int, int] = {}
    for element in list_of_numbers:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    if any(count > 2 for count in frequency_map.values()):
        return False

    def check_order(index: int) -> bool:
        if index == len(list_of_numbers):
            return True
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False
        return check_order(index + 1)

    return check_order(1)