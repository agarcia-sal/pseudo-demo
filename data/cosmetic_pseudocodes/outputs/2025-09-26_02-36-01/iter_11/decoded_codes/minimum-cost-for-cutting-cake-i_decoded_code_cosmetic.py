from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def calculateProduct(a: int, b: int) -> int:
            return a * b

        def greaterThan(x: int, y: int) -> bool:
            return not (x <= y)

        def swapDescending(arr: List[int]) -> None:
            def bubblePass(array: List[int], length: int) -> None:
                flag = False
                counter = 0
                while counter < length - 1:
                    if array[counter] < array[counter + 1]:
                        array[counter], array[counter + 1] = array[counter + 1], array[counter]
                        flag = True
                    counter += 1
                if flag:
                    bubblePass(array, length)
            bubblePass(arr, len(arr))

        result = 0
        alpha = 0
        beta = 0
        hSeg = 1
        vSeg = 1

        swapDescending(horizontalCut)
        swapDescending(verticalCut)

        def recurseProcess():
            nonlocal alpha, beta, hSeg, vSeg, result
            if alpha >= m - 1 and beta >= n - 1:
                return
            if beta == n - 1 or (alpha < m - 1 and greaterThan(horizontalCut[alpha], verticalCut[beta])):
                tempVal = calculateProduct(horizontalCut[alpha], vSeg)
                result += tempVal
                hSeg += 1
                alpha += 1
                recurseProcess()
            else:
                tempVal = calculateProduct(verticalCut[beta], hSeg)
                result += tempVal
                vSeg += 1
                beta += 1
                recurseProcess()

        recurseProcess()
        return result