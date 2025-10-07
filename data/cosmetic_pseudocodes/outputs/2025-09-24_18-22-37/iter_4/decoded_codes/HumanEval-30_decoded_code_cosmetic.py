from typing import List

def get_positive(numbers_list: List[int]) -> List[int]:
    result_list: List[int] = []
    index: int = 0
    while index < len(numbers_list):
        if numbers_list[index] > 0:
            result_list.append(numbers_list[index])
        index += 1
    return result_list