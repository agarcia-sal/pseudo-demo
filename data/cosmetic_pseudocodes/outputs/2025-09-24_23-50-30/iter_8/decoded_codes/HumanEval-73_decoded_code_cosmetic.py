from typing import List


def smallest_change(list_of_numbers: List[int]) -> int:
    count: int = 0
    limit: int = (len(list_of_numbers) - 1) // 2
    position: int = 0
    while position <= limit:
        if list_of_numbers[position] != list_of_numbers[len(list_of_numbers) - 1 - position]:
            count += 1
        position += 1
    return count