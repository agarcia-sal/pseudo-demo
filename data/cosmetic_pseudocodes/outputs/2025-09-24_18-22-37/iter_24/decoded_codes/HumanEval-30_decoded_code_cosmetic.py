from typing import List

def get_positive(numbers_list: List[int]) -> List[int]:
    result_collection: List[int] = []
    position: int = 0
    while position < len(numbers_list):
        current_value: int = numbers_list[position]
        if current_value > 0:
            result_collection.append(current_value)
        position += 1
    return result_collection