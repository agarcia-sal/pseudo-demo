from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    tally: int = 0
    midpoint: int = (len(list_of_numbers) // 2) - 1
    position: int = 0

    while position <= midpoint:
        if list_of_numbers[position] != list_of_numbers[len(list_of_numbers) - position - 1]:
            tally += 1
        position += 1

    return tally