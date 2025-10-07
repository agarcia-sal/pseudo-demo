from typing import List

def common(list_one: List[int], list_two: List[int]) -> List[int]:
    unique_common_elements = set()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                unique_common_elements.add(element_one)
    return sorted(unique_common_elements)