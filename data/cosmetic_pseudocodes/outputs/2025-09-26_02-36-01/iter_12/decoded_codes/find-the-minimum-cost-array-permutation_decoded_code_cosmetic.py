from math import inf

class Solution:
    def findPermutation(self, nums):
        lengthNums = len(nums)
        ans = []

        def depthFirstSearch(flag, previous):
            if flag == (1 << lengthNums) - 1:
                return abs(previous - nums[0])

            minimalResult = inf

            def convertLoop(index):
                nonlocal minimalResult
                if ((flag >> index) & 1) == 0:
                    interimResult = abs(previous - nums[index]) + depthFirstSearch(flag | (1 << index), index)
                    if interimResult < minimalResult:
                        minimalResult = interimResult

            for loopCounter in range(lengthNums):
                convertLoop(loopCounter)

            return minimalResult

        def graphTraverse(state, pred):
            ans.append(pred)

            if state == (1 << lengthNums) - 1:
                return

            threshold = depthFirstSearch(state, pred)

            def identifyStep(pos):
                if ((state >> pos) & 1) == 0:
                    return abs(pred - nums[pos]) + depthFirstSearch(state | (1 << pos), pos)
                return inf

            def foundNextPath(counter):
                if counter == lengthNums:
                    return False
                if identifyStep(counter) == threshold:
                    graphTraverse(state | (1 << counter), counter)
                    return True
                return foundNextPath(counter + 1)

            foundNextPath(0)

        graphTraverse(1 << 0, 0)

        return ans