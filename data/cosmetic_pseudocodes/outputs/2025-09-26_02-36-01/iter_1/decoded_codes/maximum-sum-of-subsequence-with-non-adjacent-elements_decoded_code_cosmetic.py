class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MODULUS = 10**9 + 1
        length = len(nums)

        dpSelected = [0] * length
        dpIgnored = [0] * length

        dpSelected[0] = max(0, nums[0])
        dpIgnored[0] = 0

        for i in range(1, length):
            dpSelected[i] = max(0, dpIgnored[i - 1] + nums[i])
            dpIgnored[i] = max(dpIgnored[i - 1], dpSelected[i - 1])

        resultAccumulator = 0

        for position, newValue in queries:
            nums[position] = newValue

            if position == 0:
                dpSelected[position] = max(0, nums[position])
                dpIgnored[position] = 0
            else:
                dpSelected[position] = max(0, dpIgnored[position - 1] + nums[position])
                dpIgnored[position] = max(dpIgnored[position - 1], dpSelected[position - 1])

            for index in range(position + 1, length):
                dpSelected[index] = max(0, dpIgnored[index - 1] + nums[index])
                dpIgnored[index] = max(dpIgnored[index - 1], dpSelected[index - 1])

            maxAtEnd = max(dpSelected[length - 1], dpIgnored[length - 1])
            resultAccumulator = (resultAccumulator + maxAtEnd) % MODULUS

        return resultAccumulator