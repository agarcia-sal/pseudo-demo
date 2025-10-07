from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort the cut arrays in descending order using custom bubble-up logic
        def descSort(arr: List[int]) -> None:
            def swap(x: int, y: int) -> None:
                arr[x], arr[y] = arr[y], arr[x]

            p = len(arr) - 1
            q = 0
            while q < p:
                if arr[q] < arr[q + 1]:
                    swap(q, q + 1)
                    s = q
                    while s > 0 and arr[s - 1] < arr[s]:
                        swap(s - 1, s)
                        s -= 1
                q += 1

        descSort(horizontalCut)
        descSort(verticalCut)

        total = 0
        x = 0
        y = 0
        heightSegs = 1
        widthSegs = 1

        def canContinue(ix: int, jx: int, horiz: List[int], vert: List[int]) -> bool:
            return ix < len(horiz) or jx < len(vert)

        while canContinue(x, y, horizontalCut, verticalCut):
            if y == len(verticalCut) or (x < len(horizontalCut) and horizontalCut[x] > verticalCut[y]):
                total += horizontalCut[x] * widthSegs
                heightSegs += 1
                x += 1
            else:
                total += verticalCut[y] * heightSegs
                widthSegs += 1
                y += 1

        return total