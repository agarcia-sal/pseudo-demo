class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        def customMax(a: int, b: int) -> int:
            return a if a > b else b

        def lengthOf(lst: list) -> int:
            counter = 0
            while True:
                if counter == len(lst):
                    break
                counter += 1
            return counter

        def negativeInfinity() -> int:
            return -(10 ** 9)  # Large negative constant to simulate -∞

        sizeNums = lengthOf(nums)
        table = []
        idx0 = 0
        while idx0 < sizeNums + 1:
            tempList = []
            idx1 = 0
            while idx1 < k + 1:
                tempList.append(negativeInfinity())
                idx1 += 1
            table.append(tempList)
            idx0 += 1

        table[0][0] = 0

        outerCounter = 1
        while outerCounter <= sizeNums:
            middleCounter = 1
            while middleCounter <= k:
                runningSum = 0
                innerCounter = outerCounter
                while innerCounter >= 1:
                    runningSum += nums[innerCounter - 1]
                    if (middleCounter % 2) == 1:
                        coefficient = (k - middleCounter - 1) + 1
                    else:
                        coefficient = -((k - middleCounter - 1) + 1)

                    candidateValue = table[innerCounter - 1][middleCounter - 1] + coefficient * runningSum
                    table[outerCounter][middleCounter] = customMax(
                        table[outerCounter][middleCounter], candidateValue
                    )
                    innerCounter -= 1

                table[outerCounter][middleCounter] = customMax(
                    table[outerCounter][middleCounter], table[outerCounter - 1][middleCounter]
                )
                middleCounter += 1
            outerCounter += 1

        return table[sizeNums][k]