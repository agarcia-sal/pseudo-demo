from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    freq_map: dict[int, int] = {}

    def count_occurrences(index: int) -> None:
        if index < len(list_of_numbers):
            val = list_of_numbers[index]
            freq_map[val] = freq_map.get(val, 0) + 1
            count_occurrences(index + 1)

    count_occurrences(0)

    if any(count > 2 for count in freq_map.values()):
        return False

    idx = len(list_of_numbers) - 1
    while idx > 0:
        if list_of_numbers[idx - 1] > list_of_numbers[idx]:
            return False
        idx -= 1

    return True