from typing import List


def triples_sum_to_zero(inputArray: List[int]) -> bool:
    def checkTriplets(currentA: int, currentB: int, currentC: int) -> bool:
        n = len(inputArray)
        if currentA == n:
            return False
        elif currentB == n:
            return checkTriplets(currentA + 1, currentA + 2, currentA + 3)
        elif currentC == n:
            return checkTriplets(currentA, currentB + 1, currentB + 2)
        else:
            if not (inputArray[currentA] + inputArray[currentB] + inputArray[currentC] != 0):
                return True
            else:
                return checkTriplets(currentA, currentB, currentC + 1)

    return checkTriplets(0, 1, 2)