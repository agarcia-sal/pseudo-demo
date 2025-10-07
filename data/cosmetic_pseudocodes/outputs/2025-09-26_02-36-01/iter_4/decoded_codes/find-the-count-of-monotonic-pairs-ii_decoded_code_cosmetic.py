class Solution:
    def countOfPairs(self, nums):
        modulus = 10**9 + 7
        length = len(nums)
        highest = max(nums)

        # Initialize dpList with zeros: dimensions (length+1) x (highest+1) x (highest+1)
        dpList = [[[0] * (highest + 1) for _ in range(highest + 1)] for _ in range(length + 1)]

        firstNum = nums[0]
        counter = 0
        while counter <= firstNum:
            dpList[1][counter][firstNum - counter] = 1
            counter += 1

        indexOuter = 2
        while indexOuter <= length:
            currentNum = nums[indexOuter - 1]
            jIndex = 0
            while jIndex <= currentNum:
                kIndex = 0
                while kIndex <= currentNum:
                    if (jIndex + kIndex) == currentNum:
                        prevJIndex = 0
                        while prevJIndex <= jIndex:
                            prevKIndex = kIndex
                            while prevKIndex <= highest:
                                previousValue = dpList[indexOuter - 1][prevJIndex][prevKIndex]
                                currentValue = dpList[indexOuter][jIndex][kIndex]
                                sumValue = currentValue + previousValue
                                dpList[indexOuter][jIndex][kIndex] = sumValue % modulus
                                prevKIndex += 1
                            prevJIndex += 1
                    kIndex += 1
                jIndex += 1
            indexOuter += 1

        total = 0
        outerSumIndex = 0
        while outerSumIndex <= highest:
            innerSumIndex = 0
            while innerSumIndex <= highest:
                tempSum = total + dpList[length][outerSumIndex][innerSumIndex]
                total = tempSum % modulus
                innerSumIndex += 1
            outerSumIndex += 1

        return total