from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(arg_1: List[T]) -> List[T]:
    temp_1 = Counter(arg_1)
    temp_2: List[T] = [temp_3 for temp_3 in arg_1 if temp_1[temp_3] == 1]
    return temp_2