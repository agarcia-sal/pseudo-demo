from typing import List

def strange_sort_list(numbers: List[int]) -> List[int]:
    sorted_nums: List[int] = []
    toggle: int = 1

    while numbers:
        if toggle == 1:
            chosen_value = min(numbers)
        else:
            chosen_value = max(numbers)

        sorted_nums.append(chosen_value)
        numbers = [x for x in numbers if x != chosen_value]
        toggle = 1 - toggle

    return sorted_nums