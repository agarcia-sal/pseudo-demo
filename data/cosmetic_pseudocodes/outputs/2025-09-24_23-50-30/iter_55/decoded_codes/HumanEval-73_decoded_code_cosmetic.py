from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    count: int = 0
    limit: int = (len(list_of_numbers) - 1) // 2
    counter: int = 0
    while counter <= limit:
        if not (list_of_numbers[counter] == list_of_numbers[len(list_of_numbers) - counter - 1]):
            count += 1
        counter += 1
    return count