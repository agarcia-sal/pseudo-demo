from typing import List

def will_it_fly(list_of_numbers: List[int], max_weight: int) -> bool:
    if sum(list_of_numbers) > max_weight:
        return False
    i, j = 0, len(list_of_numbers) - 1
    while i < j:
        if list_of_numbers[i] != list_of_numbers[j]:
            return False
        i += 1
        j -= 1
    return True