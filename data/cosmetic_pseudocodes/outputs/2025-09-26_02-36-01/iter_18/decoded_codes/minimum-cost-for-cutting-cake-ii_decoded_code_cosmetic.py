from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        O = 0
        P = 0
        Q = 1
        R = 1

        def SortDescending(arr: List[int]) -> None:
            lengthArr = len(arr)
            while True:
                swapped = False
                index = 1
                while index < lengthArr:
                    if arr[index - 1] < arr[index]:
                        arr[index - 1], arr[index] = arr[index], arr[index - 1]
                        swapped = True
                    index += 1
                lengthArr -= 1
                if not swapped:
                    break

        SortDescending(horizontalCut)
        SortDescending(verticalCut)

        continueLoop = True
        while continueLoop:
            if Q >= len(horizontalCut) and R >= len(verticalCut):
                continueLoop = False
            elif R == len(verticalCut) or (Q < len(horizontalCut) and horizontalCut[Q] > verticalCut[R]):
                O += horizontalCut[Q] * (P + 1)
                P += 1
                Q += 1
            else:
                O += verticalCut[R] * (Q)
                R += 1

        return O