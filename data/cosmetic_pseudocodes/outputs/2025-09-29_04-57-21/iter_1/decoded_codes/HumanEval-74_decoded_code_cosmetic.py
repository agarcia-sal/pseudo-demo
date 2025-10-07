from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_one: int = 0
    for i in range(len(list_one)):
        sum_one += len(list_one[i])
    sum_two: int = 0
    for j in list_two:
        sum_two += len(j)
    if sum_two >= sum_one:
        return list_one
    else:
        return list_two