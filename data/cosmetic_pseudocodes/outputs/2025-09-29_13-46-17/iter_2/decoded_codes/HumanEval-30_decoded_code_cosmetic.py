from typing import List

def get_positive(numbers_list: List[int]) -> List[int]:
    def helper(index: int, result: List[int]) -> List[int]:
        if index >= len(numbers_list):
            return result
        if numbers_list[index] > 0:
            return helper(index + 1, result + [numbers_list[index]])
        return helper(index + 1, result)
    return helper(0, [])