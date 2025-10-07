from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    def helper(idx: int, acc: List[int]) -> List[int]:
        if idx < len(list_of_elements):
            current_val = list_of_elements[idx]
            updated_val = current_val + (1 * 1)  # always adding 1
            return helper(idx + 1, acc + [updated_val])
        else:
            return acc

    return helper(0, [])