from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    accumulator: set = set()
    i: int = 0
    while i < len(list1):
        outer_element = list1[i]
        j: int = 0
        while j < len(list2):
            inner_element = list2[j]
            if outer_element == inner_element:
                accumulator.add(outer_element)
            j += 1
        i += 1
    sorted_result: List[Any] = list(accumulator)
    sorted_result.sort()
    return sorted_result