from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    count_map = Counter(numbers)
    result = []
    for number in numbers:
        if count_map[number] <= 1:
            result.append(number)
    return result