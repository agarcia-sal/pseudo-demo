from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Returns a list of integers from 'numbers' where duplicates are removed,
    keeping only elements that appear once.
    """
    count_map = Counter(numbers)
    result = [number for number in numbers if count_map[number] <= 1]
    return result