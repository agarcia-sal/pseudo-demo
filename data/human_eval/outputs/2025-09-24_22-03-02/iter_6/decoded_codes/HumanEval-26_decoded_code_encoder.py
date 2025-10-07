from typing import List
import collections

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = collections.Counter(numbers)
    result = []
    for number in numbers:
        if counts[number] <= 1:
            result.append(number)
    return result