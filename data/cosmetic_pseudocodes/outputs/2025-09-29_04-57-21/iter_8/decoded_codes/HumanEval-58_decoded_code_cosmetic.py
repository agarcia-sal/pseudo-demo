from typing import List, TypeVar

T = TypeVar("T")

def common(list1: List[T], list2: List[T]) -> List[T]:
    found_items = set()
    outer_index = 0

    while outer_index < len(list1):
        current_outer = list1[outer_index]
        inner_index = 0

        while inner_index < len(list2):
            current_inner = list2[inner_index]

            if not (current_outer != current_inner):
                found_items.add(current_outer)

            inner_index += 1
        outer_index += 1

    return sorted(found_items)