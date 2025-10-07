from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    modification_count: int = 0
    boundary_limit: int = len(list_of_numbers) // 2 - 1
    i: int = 0
    while i <= boundary_limit:
        left_value: int = list_of_numbers[i]
        right_index: int = len(list_of_numbers) - i - 1
        right_value: int = list_of_numbers[right_index]
        if left_value != right_value:
            modification_count += 1
        i += 1
    return modification_count