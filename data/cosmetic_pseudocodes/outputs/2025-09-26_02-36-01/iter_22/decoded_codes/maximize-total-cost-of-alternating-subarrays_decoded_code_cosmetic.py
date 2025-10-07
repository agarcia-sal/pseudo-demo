class Solution:
    def maximumTotalCost(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]

        dpList = [0] * length
        dpList[length - 1] = nums[length - 1]

        for seqPos in range(length - 2, -1, -1):
            accumulator = nums[seqPos]
            if accumulator > dpList[seqPos + 1]:
                dpList[seqPos] = accumulator
            else:
                dpList[seqPos] = dpList[seqPos + 1] + accumulator

            idx = seqPos + 1
            while idx < length:
                signVal = -1 if ((idx - seqPos) % 2) != 0 else 1
                accumulator += nums[idx] * signVal

                if idx + 1 < length:
                    compVal = accumulator + dpList[idx + 1]
                    if dpList[seqPos] < compVal:
                        dpList[seqPos] = compVal
                else:
                    if dpList[seqPos] < accumulator:
                        dpList[seqPos] = accumulator

                idx += 1

        return dpList[0]