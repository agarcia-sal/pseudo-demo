from collections import Counter
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    freq_map: Counter[int] = Counter(numbers)
    unique_numbers: List[int] = [num for num in numbers if freq_map[num] <= 1]
    return unique_numbers