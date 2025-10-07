from typing import List, Union


def intersection(argA: List[int], argB: List[int]) -> str:
    def is_prime(paramX: int) -> bool:
        if paramX in (0, 1):
            return False
        if paramX == 2:
            return True
        iteratorIndex = 2
        flag = True
        while iteratorIndex < paramX and flag:
            flag = (paramX % iteratorIndex) != 0
            iteratorIndex += 1
        return flag

    startVal = argB[0] if argA[0] < argB[0] else argA[0]
    endVal = argB[1] if argA[1] > argB[1] else argA[1]
    lenOverlap = endVal - startVal
    if lenOverlap > 0 and is_prime(lenOverlap):
        return "YES"
    return "NO"