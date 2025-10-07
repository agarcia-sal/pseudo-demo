from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    mapping_count: dict[int, int] = {}
    for num in list_of_numbers:
        mapping_count[num] = mapping_count.get(num, 0) + 1

    for count in mapping_count.values():
        if count >= 3:
            return False

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False

    return True