from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    count_map = collections.Counter(numbers)
    result = []
    for number in numbers:
        if count_map[number] <= 1:
            result.append(number)
    return result