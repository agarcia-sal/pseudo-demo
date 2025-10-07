from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    sum_two: int = 0
    for idx in range(len(list_one)):
        sum_one += len(list_one[idx])
    for idx in range(len(list_two)):
        sum_two += len(list_two[idx])
    if sum_one > sum_two:
        return list_two
    return list_one