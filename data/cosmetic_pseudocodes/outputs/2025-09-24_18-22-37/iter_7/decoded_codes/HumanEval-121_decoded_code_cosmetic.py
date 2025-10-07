from typing import List

def solution(arrA: List[int]) -> int:
    totalB: int = 0
    posC: int = 0
    while posC < len(arrA):
        if posC % 2 == 0:
            valD: int = arrA[posC]
            if valD % 2 == 1:
                totalB += valD
        posC += 1
    return totalB