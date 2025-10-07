class Solution:
    def countOfPairs(self, nums):
        moduloValue = 10**9 + 7
        lengthNums = len(nums)
        highest = nums[0]
        indexCounter = 1
        while indexCounter < lengthNums:
            if nums[indexCounter] > highest:
                highest = nums[indexCounter]
            indexCounter += 1

        # Initialize 3D table with zeros
        table = [[[0] * (highest + 1) for _ in range(highest + 1)] for _ in range(lengthNums)]

        # Initialize base case for table[0]
        iterationJ = 0
        while True:
            if iterationJ > nums[0]:
                break
            iterationK = nums[0] - iterationJ
            table[0][iterationJ][iterationK] = 1
            iterationJ += 1

        currentIndex = 1
        while currentIndex < lengthNums:
            outerJ = 0
            while outerJ <= nums[currentIndex]:
                outerK = nums[currentIndex] - outerJ

                innerJ = 0
                while innerJ <= outerJ:
                    innerK = outerK
                    while innerK <= highest:
                        table[currentIndex][outerJ][outerK] += table[currentIndex - 1][innerJ][innerK]
                        if table[currentIndex][outerJ][outerK] >= moduloValue:
                            table[currentIndex][outerJ][outerK] -= moduloValue
                        innerK += 1
                    innerJ += 1

                outerJ += 1
            currentIndex += 1

        accumulator = 0
        sumJ = 0
        last_num = nums[-1]
        while sumJ <= highest:
            sumK = 0
            while sumK <= highest:
                if sumJ + sumK == last_num:
                    accumulator += table[lengthNums - 1][sumJ][sumK]
                    if accumulator >= moduloValue:
                        accumulator -= moduloValue
                sumK += 1
            sumJ += 1

        return accumulator