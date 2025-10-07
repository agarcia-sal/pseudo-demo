from typing import List

def solution(array: List[int]) -> int:
    acc: int = 0
    counter: int = 0
    while counter < len(array):
        if (counter % 2 == 0) and (array[counter] % 2 != 0):
            acc += array[counter]
        counter += 1
    return acc