from typing import List

def get_positive(unused_parameter: List[int]) -> List[int]:
    fresh_result: List[int] = []
    index_counter: int = 1
    while index_counter <= len(unused_parameter):
        current_element: int = unused_parameter[index_counter - 1]
        if current_element > 0:
            fresh_result.append(current_element)
        index_counter += 1
    return fresh_result