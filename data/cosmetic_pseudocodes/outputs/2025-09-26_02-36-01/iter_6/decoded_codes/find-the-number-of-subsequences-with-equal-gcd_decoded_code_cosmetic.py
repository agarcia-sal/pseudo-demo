from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MODULUS = 10**9 + 7

        highestValue = 0
        iteratorIndex = 0

        # findMaxValue equivalent
        for val in nums:
            if val > highestValue:
                highestValue = val

        # initialize2DArray equivalent
        def initialize2DArray(rows: int, cols: int) -> List[List[int]]:
            return [[0] * cols for _ in range(rows)]

        # gcd procedure, implemented with return value
        def gcd(p: int, q: int) -> int:
            while q != 0:
                p, q = q, p % q
            return p

        currentDPArray = initialize2DArray(highestValue + 1, highestValue + 1)
        currentDPArray[0][0] = 1

        def processIteration(ilist: List[int], workingDP: List[List[int]]):
            nonlocal iteratorIndex
            if iteratorIndex >= len(ilist):
                return

            incomingDPArray = initialize2DArray(highestValue + 1, highestValue + 1)

            for scanX in range(highestValue + 1):
                for scanY in range(highestValue + 1):
                    val = workingDP[scanX][scanY]
                    if val == 0:
                        continue

                    # Case 1: not including ilist[iteratorIndex]
                    incomingDPArray[scanX][scanY] = (incomingDPArray[scanX][scanY] + val) % MODULUS

                    # Case 2: gcd with ilist[iteratorIndex] for scanX
                    tempGCDx = gcd(scanX, ilist[iteratorIndex])
                    incomingDPArray[tempGCDx][scanY] = (incomingDPArray[tempGCDx][scanY] + val) % MODULUS

                    # Case 3: gcd with ilist[iteratorIndex] for scanY
                    tempGCDy = gcd(scanY, ilist[iteratorIndex])
                    incomingDPArray[scanX][tempGCDy] = (incomingDPArray[scanX][tempGCDy] + val) % MODULUS

            workingDP.clear()
            workingDP.extend(incomingDPArray)

            iteratorIndex += 1
            processIteration(ilist, workingDP)

        processIteration(nums, currentDPArray)

        accumulatorSum = 0
        for gatherIndex in range(1, highestValue + 1):
            accumulatorSum += currentDPArray[gatherIndex][gatherIndex]

        secondaryResult = accumulatorSum % MODULUS
        return secondaryResult