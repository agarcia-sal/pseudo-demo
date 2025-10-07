from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    # Increment the head of the list by 1, recursively process the tail
    def helper(sOf: List[int], kx: List[int]) -> List[int]:
        if sOf:
            return [sOf[0] + 1] + helper(sOf[1:], kx)
        else:
            return []

    New_lambda = helper(list_of_elements, list_of_elements)
    Yd_s = New_lambda
    return Yd_s