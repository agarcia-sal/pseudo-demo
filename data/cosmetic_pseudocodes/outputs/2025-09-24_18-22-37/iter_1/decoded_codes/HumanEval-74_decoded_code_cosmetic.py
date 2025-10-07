from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    sum_length_one: int = 0
    for index in range(len(list_one)):
        sum_length_one += len(list_one[index])
    sum_length_two: int = 0
    for index in range(len(list_two)):
        sum_length_two += len(list_two[index])
    if sum_length_one <= sum_length_two:
        return list_one
    else:
        return list_two