from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    counts: Dict[int, int] = {}
    index: int = 0
    while index < len(list_of_numbers):
        value = list_of_numbers[index]
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1
        index += 1

    has_value_more_than_two = False
    for num in list_of_numbers:
        count = counts.get(num, 0)
        if count > 2:
            has_value_more_than_two = True
            break

    if has_value_more_than_two:
        return False

    def _check_sorted(arr: List[int], pos: int) -> bool:
        if pos >= len(arr):
            return True
        if arr[pos - 1] > arr[pos]:
            return False
        else:
            return _check_sorted(arr, pos + 1)

    return _check_sorted(list_of_numbers, 1)