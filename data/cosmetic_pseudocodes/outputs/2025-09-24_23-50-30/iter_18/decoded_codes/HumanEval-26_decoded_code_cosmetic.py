from collections import Counter
from typing import List

def remove_duplicates(collection_of_ints: List[int]) -> List[int]:
    counts_map: Counter[int] = Counter(collection_of_ints)
    result_array: List[int] = [value for value in collection_of_ints if counts_map[value] == 1]
    return result_array