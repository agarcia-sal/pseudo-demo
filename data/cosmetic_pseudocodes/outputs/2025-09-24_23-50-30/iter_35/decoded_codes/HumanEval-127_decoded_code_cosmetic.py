from typing import List

def intersection(inputA: List[int], inputB: List[int]) -> str:
    def is_prime(checkVal: int) -> bool:
        if checkVal in (0, 1):
            return False
        if checkVal == 2:
            return True
        for index in range(2, checkVal):
            if checkVal % index == 0:
                return False
        return True

    startPoint: int = inputA[0] if inputA[0] > inputB[0] else inputB[0]
    endPoint: int = inputA[1] if inputA[1] < inputB[1] else inputB[1]
    overlap: int = endPoint - startPoint

    if (overlap > 0) and is_prime(overlap):
        return "YES"
    return "NO"