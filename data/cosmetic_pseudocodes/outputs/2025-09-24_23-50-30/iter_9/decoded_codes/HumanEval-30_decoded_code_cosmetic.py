from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    result: List[float] = []
    for each_item in list_of_numbers:
        if each_item > 0:
            result.append(each_item)
    return result