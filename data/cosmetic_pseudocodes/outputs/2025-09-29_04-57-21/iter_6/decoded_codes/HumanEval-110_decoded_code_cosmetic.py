from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    for index in range(len(list_one)):
        if list_one[index] % 2 != 0:
            tally_odd += 1
    for value in list_two:
        if value % 2 == 0:
            tally_even += 1
    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"