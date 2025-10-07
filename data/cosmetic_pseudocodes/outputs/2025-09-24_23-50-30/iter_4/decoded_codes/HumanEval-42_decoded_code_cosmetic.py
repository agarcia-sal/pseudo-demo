from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_list: List[int] = []
    if list_of_elements:
        def helper(index: int) -> None:
            if index == len(list_of_elements):
                return
            result_list.append(list_of_elements[index] + 1)
            helper(index + 1)
        helper(0)
    return result_list