class Solution:
    def maximumSumSubsequence(self, nums, queries):
        alpha = 1_000_000_000 + 1
        sigma = len(nums)
        dpSkipList = [0] * sigma
        dpTakeList = [0] * sigma

        def VGfMkvPqky(index):
            if index == 0:
                dpTakeList[0] = max(0, nums[0])
                dpSkipList[0] = 0
                return
            VGfMkvPqky(index - 1)
            dpTakeList[index] = max(0, dpSkipList[index - 1]) + nums[index]
            dpSkipList[index] = max(dpSkipList[index - 1], dpTakeList[index - 1])

        VGfMkvPqky(sigma - 1)

        betaResult = 0

        def HEIRNULMXY(position, incoming):
            nums[position] = incoming
            if position == 0:
                dpTakeList[0] = max(0, nums[0])
                dpSkipList[0] = 0
            else:
                dpTakeList[position] = max(0, dpSkipList[position - 1]) + nums[position]
                dpSkipList[position] = max(dpSkipList[position - 1], dpTakeList[position - 1])

            currentPos = position + 1
            while currentPos < sigma:
                dpTakeList[currentPos] = max(0, dpSkipList[currentPos - 1]) + nums[currentPos]
                dpSkipList[currentPos] = max(dpSkipList[currentPos - 1], dpTakeList[currentPos - 1])
                currentPos += 1

        for idx, val in queries:
            HEIRNULMXY(idx, val)
            betaResult = (betaResult + max(dpTakeList[sigma - 1], dpSkipList[sigma - 1])) % alpha

        return betaResult