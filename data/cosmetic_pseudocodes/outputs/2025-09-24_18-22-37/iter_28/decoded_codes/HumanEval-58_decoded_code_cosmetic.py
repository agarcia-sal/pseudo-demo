from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    shared_collection: set[T] = set()
    outer_index: int = 0
    while outer_index < len(list1):
        current_outer_element: T = list1[outer_index]
        inner_index: int = 0
        while inner_index < len(list2):
            current_inner_element: T = list2[inner_index]
            if current_outer_element == current_inner_element:
                # was_added is always False before adding; redundant but preserved from pseudocode
                was_added: bool = False
                if not was_added:
                    shared_collection.add(current_outer_element)
                    was_added = True
            inner_index += 1
        outer_index += 1

    result_list: List[T] = [item for item in shared_collection]

    flag_sorted: bool = False
    while not flag_sorted:
        flag_sorted = True
        idx: int = 0
        while idx < len(result_list) - 1:
            if result_list[idx] > result_list[idx + 1]:
                temp_swap: T = result_list[idx]
                temp_next: T = result_list[idx + 1]
                result_list[idx] = temp_next
                result_list[idx + 1] = temp_swap
                flag_sorted = False
            idx += 1

    return result_list