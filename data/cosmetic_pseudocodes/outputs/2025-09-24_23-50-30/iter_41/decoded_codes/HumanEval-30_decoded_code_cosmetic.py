from typing import List

def get_positive(input_list: List[int]) -> List[int]:
    return [each_item for each_item in input_list if each_item > 0]