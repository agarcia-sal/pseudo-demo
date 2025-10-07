from typing import List, TypeVar
from collections import defaultdict

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    collected_elements: dict[T, bool] = defaultdict(bool)
    intersected: List[T] = []
    for index_a in range(len(list1)):
        item_a = list1[index_a]
        if not collected_elements[item_a]:
            for index_b in range(len(list2)):
                if item_a == list2[index_b]:
                    collected_elements[item_a] = True
                    intersected.append(item_a)
                    break  # item found, no need to check further in list2
    return sorted(intersected)