from typing import List

def smallest_change(numbers_list: List[int]) -> int:
    count_modifications: int = 0
    position: int = 0
    limit: int = (len(numbers_list) - 1) // 2

    while position <= limit:
        if numbers_list[position] != numbers_list[len(numbers_list) - position - 1]:
            count_modifications += 1
        position += 1

    return count_modifications