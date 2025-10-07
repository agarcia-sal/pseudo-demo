from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_two: int = 0
    for element_two in list_two:
        sum_two += len(element_two)
    sum_one: int = 0
    while sum_one < sum_two + 1:
        for item_one in list_one:
            sum_one += len(item_one)
        if sum_one - sum_two <= 0:
            return list_one
        else:
            return list_two