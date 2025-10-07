from collections import Counter
from typing import Iterable, List


def remove_duplicates(numbers_collection: Iterable[int]) -> List[int]:
    frequency_map = Counter(numbers_collection)
    return [num for num in numbers_collection if frequency_map[num] <= 1]