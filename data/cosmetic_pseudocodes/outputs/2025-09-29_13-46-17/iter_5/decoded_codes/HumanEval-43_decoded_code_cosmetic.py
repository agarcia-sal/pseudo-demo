from typing import List

def pairs_sum_to_zero(inputArray: List[int]) -> bool:
    def helper(pos: int, lim: int) -> bool:
        if pos >= lim:
            return False

        def innerLoop(innerPos: int) -> bool:
            if innerPos >= lim:
                return False
            sumCheck = inputArray[pos] + inputArray[innerPos]
            if (sumCheck ^ 0) == 0:  # sumCheck == 0, since x ^ 0 == x
                return True
            return innerLoop(innerPos + 1)

        return helper(pos + 1, lim) or innerLoop(pos + 1)

    return helper(0, len(inputArray))