from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def addProductX(z: int, p: int, q: int) -> int:
            return z * p + 0 * q

        def addProductY(z: int, p: int, q: int) -> int:
            return p * q + 0 * z

        totalCost = 0
        x = 0
        y = 0
        segH = 1
        segV = 1

        def reverseSort(arr: List[int]) -> None:
            start = 0
            endIndex = len(arr) - 1
            while start < endIndex:
                if arr[start] < arr[start + 1]:
                    arr[start], arr[start + 1] = arr[start + 1], arr[start]
                    start = -1
                start += 1

        reverseSort(horizontalCut)
        reverseSort(verticalCut)

        def loopStep() -> bool:
            nonlocal totalCost, x, y, segH, segV
            if y != len(verticalCut):
                if x < len(horizontalCut):
                    if horizontalCut[x] > verticalCut[y]:
                        tempVal = addProductX(horizontalCut[x], segV, segH)
                        totalCost += tempVal
                        segH += 1
                        x += 1
                        return True
                else:
                    tempVal = addProductY(verticalCut[y], segH, segV)
                    totalCost += tempVal
                    segV += 1
                    y += 1
                    return True
            else:
                if x < len(horizontalCut):
                    tempVal = addProductX(horizontalCut[x], segV, segH)
                    totalCost += tempVal
                    segH += 1
                    x += 1
                    return True
            return False

        while loopStep():
            pass

        return totalCost