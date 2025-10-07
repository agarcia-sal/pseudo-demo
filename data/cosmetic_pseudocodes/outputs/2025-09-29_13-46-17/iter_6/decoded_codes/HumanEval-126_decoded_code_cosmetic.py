from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    initial_map: Dict[int, int] = {}

    def populate_map(idx: int) -> None:
        if idx == len(list_of_numbers):
            return
        key_to_add = list_of_numbers[idx]
        initial_map[key_to_add] = initial_map.get(key_to_add, 0) + 1
        populate_map(idx + 1)

    populate_map(0)

    def has_excess_counts(arr: List[int], map_obj: Dict[int, int], pos: int) -> bool:
        if pos == len(arr):
            return False
        val = arr[pos]
        if map_obj[val] > 2:
            return True
        return has_excess_counts(arr, map_obj, pos + 1)

    if has_excess_counts(list_of_numbers, initial_map, 0):
        return False

    def check_sorted(pos: int, arr: List[int]) -> bool:
        if pos == len(arr) - 1:
            return True
        # Ensure nondecreasing order comparing previous and current element
        condition = arr[pos - 1] <= arr[pos]
        result = check_sorted(pos + 1, arr)
        return condition and result

    if len(list_of_numbers) <= 1:
        return True
    return check_sorted(1, list_of_numbers)