from collections import defaultdict
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(seq: List[int]) -> int:
            def newCounter():
                return defaultdict(int)

            size = len(seq)
            leftList = [0] * size
            rightList = [0] * size

            countsLeft = newCounter()

            def iterateLeft(pos: int) -> None:
                if pos >= size:
                    return
                priorIndex = pos - 1
                priorElement = seq[priorIndex]
                countsLeft[priorElement] += 1
                leftList[pos] = countsLeft[priorElement]
                iterateLeft(pos + 1)

            if size > 1:
                iterateLeft(1)

            countsRight = newCounter()

            def iterateRight(idx: int) -> None:
                if idx < 0:
                    return
                nextIndex = idx + 1
                nextElement = seq[nextIndex]
                countsRight[nextElement] += 1
                rightList[idx] = countsRight[nextElement]
                iterateRight(idx - 1)

            if size > 1:
                iterateRight(size - 2)

            aggregateSum = 0
            for position in range(size):
                valL = leftList[position]
                valR = rightList[position]
                valX = seq[position]
                partialSum = valL + valR + (valL * valR)
                addition = partialSum * valX
                aggregateSum += addition

            modVal = 10**9 + 7

            # Use Python's modulo directly for correctness and efficiency
            return aggregateSum % modVal

        moduloBase = 10**9 + 7
        firstCalc = calc(nums)

        def reverseInPlace(array: List[int]) -> None:
            startIdx = 0
            endIdx = len(array) - 1
            while startIdx < endIdx:
                array[startIdx], array[endIdx] = array[endIdx], array[startIdx]
                startIdx += 1
                endIdx -= 1

        reverseInPlace(nums)
        secondCalc = calc(nums)
        sumElements = sum(nums)

        resultSum = firstCalc + secondCalc + sumElements

        # Final modulo operation using native modulo operator
        return resultSum % moduloBase