from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd: int = 0
    count_even: int = 0
    for element in list_one:
        if element % 2 == 1:
            count_odd += 1
    for element in list_two:
        if element % 2 == 0:
            count_even += 1
    if count_even >= count_odd:
        return "YES"
    return "NO"