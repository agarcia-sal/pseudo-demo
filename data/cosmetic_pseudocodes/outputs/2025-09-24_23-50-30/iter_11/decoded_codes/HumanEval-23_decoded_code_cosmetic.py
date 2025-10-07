from typing import Iterable

def strlen(input: Iterable) -> int:
    tempResult: int = 0
    for eachChar in input:
        tempResult += 1
    return tempResult