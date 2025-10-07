class Solution:
    def subsequencePairCount(self, nums):
        THRESHOLD = 10**9 + 7
        omega = 0
        for alpha in nums:
            if alpha > omega:
                omega = alpha

        def buildGrid(rows, cols):
            # Create a grid of zeros with dimensions rows x cols
            return [[0] * cols for _ in range(rows)]

        zeta = buildGrid(omega + 1, omega + 1)
        zeta[0][0] += 1

        def gcdUtil(a, b):
            while b:
                a, b = b, a % b
            return a

        stateMatrix = zeta

        def advanceState(currMatrix, item):
            nextMatrix = buildGrid(omega + 1, omega + 1)
            for iIndex in range(omega + 1):
                for jIndex in range(omega + 1):
                    val = currMatrix[iIndex][jIndex]
                    if val == 0:
                        continue
                    # Add current state count
                    nextMatrix[iIndex][jIndex] += val
                    if nextMatrix[iIndex][jIndex] >= THRESHOLD:
                        nextMatrix[iIndex][jIndex] -= THRESHOLD

                    # Update gcd for i
                    iNew = gcdUtil(iIndex, item)
                    nextMatrix[iNew][jIndex] += val
                    if nextMatrix[iNew][jIndex] >= THRESHOLD:
                        nextMatrix[iNew][jIndex] -= THRESHOLD

                    # Update gcd for j
                    jNew = gcdUtil(jIndex, item)
                    nextMatrix[iIndex][jNew] += val
                    if nextMatrix[iIndex][jNew] >= THRESHOLD:
                        nextMatrix[iIndex][jNew] -= THRESHOLD

            return nextMatrix

        def processAll(numbers):
            if not numbers:
                return stateMatrix
            firstNum = numbers[0]
            suffix = numbers[1:]
            nextMatrix = processAll(suffix)
            return advanceState(nextMatrix, firstNum)

        stateMatrix = processAll(nums)

        accumulator = 0
        for gIndex in range(1, omega + 1):
            accumulator += stateMatrix[gIndex][gIndex]
        if accumulator >= THRESHOLD:
            accumulator %= THRESHOLD

        return accumulator