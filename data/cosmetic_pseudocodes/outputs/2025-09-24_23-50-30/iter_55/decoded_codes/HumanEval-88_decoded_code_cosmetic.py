from typing import List

def sort_array(input_collection: List[int]) -> List[int]:
    if not len(input_collection) > 0:
        return []
    temp_sum: int = input_collection[0] + input_collection[len(input_collection) - 1]
    descending_flag: bool = (temp_sum % 2) == 0
    return sorted(input_collection, reverse=descending_flag)