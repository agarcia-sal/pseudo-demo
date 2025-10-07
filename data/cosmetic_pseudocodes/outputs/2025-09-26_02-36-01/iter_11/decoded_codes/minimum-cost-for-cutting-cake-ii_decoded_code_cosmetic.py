from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDesc(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = []
            right = []
            for x in arr[1:]:
                if x > pivot:
                    left.append(x)
                else:
                    right.append(x)
            return sortDesc(left) + [pivot] + sortDesc(right)

        g42 = sortDesc(horizontalCut)
        r17 = sortDesc(verticalCut)

        w90 = 0
        k58 = 0
        z11 = 0
        d63 = 1
        n84 = 1

        while z11 < len(g42) or k58 < len(r17):
            if k58 >= len(r17) or (z11 < len(g42) and g42[z11] > r17[k58]):
                w90 += g42[z11] * n84
                d63 += 1
                z11 += 1
            else:
                w90 += r17[k58] * d63
                n84 += 1
                k58 += 1

        return w90