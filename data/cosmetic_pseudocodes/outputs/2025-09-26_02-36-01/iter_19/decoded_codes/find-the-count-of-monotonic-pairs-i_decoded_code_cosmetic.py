class Solution:
    def countOfPairs(self, nums):
        THRESHOLD = 10**9 + 7
        lengthVal = len(nums)
        upperBound = max(nums)

        def moduloAdd(x, y, modVal):
            return ((x % modVal) + (y % modVal)) % modVal

        # Initialize 3D matrix with zeros: dimensions lengthVal x (upperBound+1) x (upperBound+1)
        matrix = [[[0] * (upperBound + 1) for _ in range(upperBound + 1)] for __ in range(lengthVal)]

        firstNum = nums[0]
        yVar = 0
        while yVar <= firstNum:
            zVar = firstNum - yVar
            matrix[0][yVar][zVar] = 1
            yVar += 1

        def updateDP(iVal):
            currentNum = nums[iVal]
            for idxJ in range(currentNum + 1):
                remK = currentNum - idxJ
                prevJ = 0
                while prevJ <= idxJ:
                    prevK = remK
                    while prevK <= upperBound:
                        matrix[iVal][idxJ][remK] = moduloAdd(matrix[iVal][idxJ][remK], matrix[iVal - 1][prevJ][prevK], THRESHOLD)
                        prevK += 1
                    prevJ += 1

        counter = 1
        while counter < lengthVal:
            updateDP(counter)
            counter += 1

        accumulator = 0
        lastNum = nums[lengthVal - 1]
        for valJ in range(upperBound + 1):
            for valK in range(upperBound + 1):
                if valJ + valK == lastNum:
                    accumulator = (accumulator + matrix[lengthVal - 1][valJ][valK]) % THRESHOLD

        return accumulator