class Solution:
    def sumOfPower(self, nums, k):
        CONST_MODULUS = 10**9 + 7
        LENGTH_VAR = len(nums)
        MEMORY_TABLE = []

        def initializeMemory():
            nonlocal MEMORY_TABLE
            MEMORY_TABLE = [[0 for _ in range(k + 1)] for _ in range(LENGTH_VAR + 1)]
            MEMORY_TABLE[0][0] = 1

        def populateMemory(current):
            if current > LENGTH_VAR:
                return
            iterator = 0
            currentRow = MEMORY_TABLE[current]
            previousRow = MEMORY_TABLE[current - 1]
            while iterator <= k:
                currentRow[iterator] = previousRow[iterator]
                if iterator >= nums[current - 1]:
                    currentRow[iterator] = (currentRow[iterator] + previousRow[iterator - nums[current - 1]]) % CONST_MODULUS
                else:
                    currentRow[iterator] %= CONST_MODULUS
                iterator += 1
            populateMemory(current + 1)

        def summary():
            accumulator = 0
            subsetIndex = 1
            limit = (1 << LENGTH_VAR) - 1
            while subsetIndex <= limit:
                sumTracker = 0
                elementCounter = 0
                positionPointer = 0
                mask = subsetIndex
                while mask > 0:
                    if mask & 1:
                        sumTracker += nums[positionPointer]
                        elementCounter += 1
                    mask >>= 1
                    positionPointer += 1
                if sumTracker == k:
                    accumulator = (accumulator + pow(2, LENGTH_VAR - elementCounter, CONST_MODULUS)) % CONST_MODULUS
                subsetIndex += 1
            return accumulator

        initializeMemory()
        populateMemory(1)
        return summary()