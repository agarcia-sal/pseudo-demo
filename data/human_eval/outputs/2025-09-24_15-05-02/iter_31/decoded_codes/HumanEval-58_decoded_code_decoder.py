from typing import List

def common(list_one: List[int], list_two: List[int]) -> List[int]:
    result_set = set()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                result_set.add(element_one)
    return sorted(result_set)