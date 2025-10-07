class Solution:
    def maximumSumSubsequence(self, nums, queries):
        P = 10**9 + 1
        lengthVar = len(nums)
        includedArrays = [0] * lengthVar
        excludedArrays = [0] * lengthVar

        includedArrays[0] = nums[0] if nums[0] > 0 else 0
        excludedArrays[0] = 0

        for i in range(1, lengthVar):
            includedArrays[i] = excludedArrays[i - 1] + nums[i]
            if includedArrays[i] < 0:
                includedArrays[i] = 0
            excludedArrays[i] = max(excludedArrays[i - 1], includedArrays[i - 1])

        aggregateResult = 0

        for position, newValue in queries:
            nums[position] = newValue
            if position == 0:
                includedArrays[position] = nums[position] if nums[position] > 0 else 0
                excludedArrays[position] = 0
            else:
                includedArrays[position] = excludedArrays[position - 1] + nums[position]
                if includedArrays[position] < 0:
                    includedArrays[position] = 0
                excludedArrays[position] = max(excludedArrays[position - 1], includedArrays[position - 1])

            iPos = position + 1
            while iPos < lengthVar:
                includedArrays[iPos] = excludedArrays[iPos - 1] + nums[iPos]
                if includedArrays[iPos] < 0:
                    includedArrays[iPos] = 0
                excludedArrays[iPos] = max(excludedArrays[iPos - 1], includedArrays[iPos - 1])
                iPos += 1

            maxAtEnd = max(includedArrays[lengthVar - 1], excludedArrays[lengthVar - 1])
            aggregateResult = (aggregateResult + maxAtEnd) % P

        return aggregateResult