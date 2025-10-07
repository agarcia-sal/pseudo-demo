class Solution:
    def subsequencePairCount(self, nums):
        modVal = 10_000_000_007
        maxVal = 0
        idxCounter = 0

        while idxCounter < len(nums):
            if nums[idxCounter] > maxVal:
                maxVal = nums[idxCounter]
            idxCounter += 1

        dpTable = self.CREATE_2D_ARRAY(maxVal + 1, maxVal + 1, 0)
        dpTable[0][0] = 1

        def gcdFunction(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        idxA = 0
        while idxA < len(nums):
            currentNum = nums[idxA]
            nextDp = self.CREATE_2D_ARRAY(maxVal + 1, maxVal + 1, 0)

            xVal = 0
            while xVal <= maxVal:
                yVal = 0
                while yVal <= maxVal:
                    currentDPVal = dpTable[xVal][yVal]

                    # Add current value to nextDp at (xVal, yVal)
                    nextDp[xVal][yVal] = (nextDp[xVal][yVal] + currentDPVal) % modVal

                    # Add current value to nextDp at (gcd(xVal, currentNum), yVal)
                    gX = gcdFunction(xVal, currentNum)
                    nextDp[gX][yVal] = (nextDp[gX][yVal] + currentDPVal) % modVal

                    # Add current value to nextDp at (xVal, gcd(yVal, currentNum))
                    gY = gcdFunction(yVal, currentNum)
                    nextDp[xVal][gY] = (nextDp[xVal][gY] + currentDPVal) % modVal

                    yVal += 1
                xVal += 1

            dpTable = nextDp
            idxA += 1

        answerTotal = 0
        gIndex = 1
        while True:
            if gIndex > maxVal:
                break
            answerTotal += dpTable[gIndex][gIndex]
            gIndex += 1

        finalAnswer = answerTotal % modVal
        return finalAnswer

    def CREATE_2D_ARRAY(self, rows, cols, initialValue):
        return [[initialValue for _ in range(cols)] for _ in range(rows)]