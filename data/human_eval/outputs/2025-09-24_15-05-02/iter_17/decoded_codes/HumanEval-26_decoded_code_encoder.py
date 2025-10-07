from typing import List
import collections

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    c: collections.Counter = collections.Counter(list_of_numbers)
    result: List[int] = []
    for number in list_of_numbers:
        if c[number] <= 1:
            result.append(number)
    return result