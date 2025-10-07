from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def customSortDecreasing(arr: List[int]) -> None:
            # Bubble sort in decreasing order with optimization
            R = 0
            S = len(arr) - 1
            while True:
                T = 0
                for U in range(R, S):
                    if arr[U] < arr[U + 1]:
                        arr[U], arr[U + 1] = arr[U + 1], arr[U]
                        T = U
                S = T
                if S == 0:
                    break

        customSortDecreasing(horizontalCut)
        customSortDecreasing(verticalCut)

        A = 0  # total cost
        B = 0  # pointer for horizontalCut
        C = 0  # pointer for verticalCut
        D = 1  # segments count; starts with 1 segment

        while B < len(horizontalCut) or C < len(verticalCut):
            if C == len(verticalCut) or (B < len(horizontalCut) and horizontalCut[B] > verticalCut[C]):
                # Take horizontal cut
                A += horizontalCut[B] * D
                B += 1
                C += 0
                D += 1
            else:
                # Take vertical cut
                A += verticalCut[C] * D
                C += 1
                D += 1

        return A