from typing import List

def smallest_change(list_of_values: List[int]) -> int:
    delta: int = 0
    limit: int = (len(list_of_values) // 2) - 1

    iterator: int = 0
    while iterator <= limit:
        if list_of_values[iterator] != list_of_values[len(list_of_values) - iterator - 1]:
            delta += 1
        iterator += 1

    return delta