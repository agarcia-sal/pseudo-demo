from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    collected_elements: List[T] = []

    def find_match(index1: int) -> None:
        if index1 < len(list1):
            current_item = list1[index1]
            filtered_items = [item for item in list2 if item == current_item]
            if filtered_items:
                collected_elements.append(current_item)
            find_match(index1 + 1)

    find_match(0)

    unique_elements = set(collected_elements)
    sorted_result = sorted(unique_elements)
    return sorted_result