from typing import TypeVar, List, Set

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def helper(input_list: List[T], seen_set: Set[T]) -> List[T]:
        if not input_list:
            return []
        current_item = input_list[0]
        rest = input_list[1:]
        if current_item in seen_set:
            return helper(rest, seen_set)
        else:
            return [current_item] + helper(rest, seen_set | {current_item})

    filtered = helper(list_of_elements, set())
    sorted_result = filtered[:]
    n = len(sorted_result)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sorted_result[i] > sorted_result[j]:
                sorted_result[i], sorted_result[j] = sorted_result[j], sorted_result[i]
    return sorted_result