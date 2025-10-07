from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    countOdd: int = 0
    countEven: int = 0
    i: int = 0
    while i < len(list_one):
        if list_one[i] % 2 == 1:
            countOdd += 1
        i += 1
    i = 0
    while i < len(list_two):
        if list_two[i] % 2 == 0:
            countEven += 1
        i += 1
    if countEven >= countOdd:
        output: str = "YES"
    else:
        output = "NO"
    return output