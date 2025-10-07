from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def check_sorted_rec(index: int, values: List[int]) -> bool:
        if index == len(values):
            return True
        if values[index - 1] > values[index]:
            return False
        return check_sorted_rec(index + 1, values)

    frequency_map: Dict[int, int] = {}
    for num in list_of_numbers:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for key in frequency_map:
        if frequency_map[key] > 2:
            return False

    return check_sorted_rec(1, list_of_numbers)