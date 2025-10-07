from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator: set[T] = set()
    outer_index: int = 0
    while outer_index < len(list1):
        current_item = list1[outer_index]
        inner_iterator: int = 0
        while inner_iterator < len(list2):
            if not (current_item != list2[inner_iterator]):
                accumulator.add(current_item)
            inner_iterator += 1
        outer_index += 1
    return sorted(accumulator)