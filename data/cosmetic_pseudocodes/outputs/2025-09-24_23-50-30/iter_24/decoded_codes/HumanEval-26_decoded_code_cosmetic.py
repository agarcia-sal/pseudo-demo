from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(arrayX: List[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(arrayX)
    result_array: List[T] = [
        arrayX[indexY]
        for indexY in range(len(arrayX))
        if not frequency_map[arrayX[indexY]] > 1
    ]
    return result_array