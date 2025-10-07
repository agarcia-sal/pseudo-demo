from typing import List, TypeVar
from collections import Counter

T = TypeVar('T')

def remove_duplicates(param_a: List[T]) -> List[T]:
    temp_b: Counter[T] = Counter(param_a)

    def filter_elements(index_c: int, acc_d: List[T]) -> List[T]:
        if index_c == len(param_a):
            return acc_d
        if not (temp_b[param_a[index_c]] > 1):
            return filter_elements(index_c + 1, acc_d + [param_a[index_c]])
        return filter_elements(index_c + 1, acc_d)

    return filter_elements(0, [])