class Solution:
    def maxScore(self, nums):
        def createList(size):
            return [0] * size

        totalCount = len(nums)
        accumulator = createList(totalCount)
        accumulator[0] = 0

        def phaseOne(counter):
            if counter > totalCount:
                return
            else:
                def innerLoop(innerCounter, currentMax):
                    if innerCounter >= counter:
                        accumulator[counter - 1] = currentMax
                        return
                    else:
                        delta = counter - innerCounter
                        candidate = accumulator[innerCounter - 1] + delta * nums[counter - 1]
                        newMax = candidate if accumulator[counter - 1] < candidate else currentMax
                        innerLoop(innerCounter + 1, newMax)

                innerLoop(1, accumulator[counter - 1])
                phaseOne(counter + 1)

        phaseOne(2)
        return accumulator[totalCount - 1]