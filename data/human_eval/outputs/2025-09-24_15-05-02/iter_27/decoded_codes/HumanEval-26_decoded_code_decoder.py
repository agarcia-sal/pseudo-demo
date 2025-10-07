from typing import List
import collections

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    counts: collections.Counter[int] = collections.Counter(list_of_numbers)
    unique_numbers: List[int] = [number for number in list_of_numbers if counts[number] <= 1]
    return unique_numbers