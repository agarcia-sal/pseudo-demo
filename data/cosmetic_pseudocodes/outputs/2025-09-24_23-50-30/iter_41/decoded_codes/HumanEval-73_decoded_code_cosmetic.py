from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    count_result: int = 0
    limit: int = len(list_of_numbers) // 2
    cursor: int = 0
    while cursor < limit:
        if list_of_numbers[cursor] != list_of_numbers[len(list_of_numbers) - cursor - 1]:
            count_result += 1
        cursor += 1
    return count_result