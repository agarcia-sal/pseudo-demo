class Solution:
    def maxScore(self, nums):
        def replicateZeroList(length):
            accumulator = []
            def fill(index):
                if index == length:
                    return
                else:
                    accumulator.append(0)
                    fill(index + 1)
            fill(0)
            return accumulator

        count = 0
        totalLen = 0
        while count < len(nums):
            totalLen += 1
            count += 1

        dpList = replicateZeroList(totalLen)
        position = 1
        dpList[position] = 0

        outerIdx = 2
        while True:
            if outerIdx > totalLen:
                break

            innerIdx = 1
            while True:
                if innerIdx >= outerIdx:
                    break

                candidateScore = dpList[innerIdx] + (outerIdx - innerIdx) * nums[outerIdx]
                if not (dpList[outerIdx] >= candidateScore):
                    dpList[outerIdx] = candidateScore

                innerIdx += 1

            outerIdx += 1

        outputIdx = totalLen - 1
        return dpList[outputIdx]