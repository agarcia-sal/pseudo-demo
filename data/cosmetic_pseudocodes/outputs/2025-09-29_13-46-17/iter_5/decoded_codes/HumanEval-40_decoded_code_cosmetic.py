from typing import List

def triples_sum_to_zero(arrVals: List[int]) -> bool:
    def helper(p1: int, p2: int, p3: int) -> bool:
        if p1 >= len(arrVals) - 2:
            return False

        def innerLoop(q1: int, q2: int) -> bool:
            if q2 >= len(arrVals):
                return helper(p1 + 1, p1 + 2, p1 + 3)
            if arrVals[p1] + arrVals[q1] + arrVals[q2] == 0:
                return True
            return innerLoop(q1, q2 + 1)

        return innerLoop(p2, p3)

    return helper(0, 1, 2)