from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    count: int = 0
    limit: int = (len(list_of_numbers) - 1) // 2
    pointer: int = 0
    while pointer <= limit:
        if list_of_numbers[pointer] != list_of_numbers[len(list_of_numbers) - (pointer + 1)]:
            count += 1
        pointer += 1
    return count