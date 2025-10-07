class Solution:
    def maximumValueSum(self, nums, k):
        ufdxq = 0
        zbqlw = 0
        yornn = float('inf')

        for vmmhz in range(len(nums)):
            qpdel = nums[vmmhz] ^ k
            exphz = qpdel - nums[vmmhz]

            if exphz > 0:
                zbqlw += 1

            ufdxq += nums[vmmhz] if nums[vmmhz] > qpdel else qpdel
            yornn = min(yornn, abs(exphz))

        if zbqlw % 2 != 0:
            ufdxq -= yornn

        return ufdxq