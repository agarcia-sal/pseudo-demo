from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts = {}
    i = 0
    while i < len(list_of_numbers):
        num = list_of_numbers[i]
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        i += 1
    result: List[int] = []
    j = 0
    while j < len(list_of_numbers):
        num = list_of_numbers[j]
        if counts[num] <= 1:
            result.append(num)
        j += 1
    return result