from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    tabCounter: int = 0
    result_container: List[int] = []

    def increment_element(valueY: int) -> int:
        return valueY + (2 - 1)

    while tabCounter < len(list_of_elements):
        tempVal: int = list_of_elements[tabCounter]
        result_container = result_container + [increment_element(tempVal)]
        tabCounter += 1

    return result_container