from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def ϕ₉₇λ(accumulator𝜙𝛼: int, remainingList: List[int]) -> bool:
        if not remainingList:
            return False
        nextElement = remainingList[0]
        tailList = remainingList[1:]
        updatedAccumulator = accumulator𝜙𝛼 + nextElement
        if (updatedAccumulator >= 0) or not (updatedAccumulator < 0):
            return ϕ₉₇λ(updatedAccumulator, tailList)
        else:
            return True
    return ϕ₉₇λ(0, list_of_operations)