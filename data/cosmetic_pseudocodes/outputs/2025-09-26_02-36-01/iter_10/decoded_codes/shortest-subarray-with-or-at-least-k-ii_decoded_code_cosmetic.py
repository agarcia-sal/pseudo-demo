class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def adjustBits(freq: list[int], val: int, diff: int) -> None:
            bitFlag = 1
            idx = 0
            while idx <= 31:
                if (val & bitFlag) != 0:
                    freq[idx] += diff
                bitFlag <<= 1
                idx += 1

        def gatherOr(freq: list[int]) -> int:
            acc = 0
            pos = 0
            while pos <= 31:
                if freq[pos] > 0:
                    acc |= (1 << pos)
                pos += 1
            return acc

        lengthNums = len(nums)
        bitCounts = [0] * 32
        combinedOr = 0
        startPtr = 0
        minimalDist = float('inf')

        endPtr = 0
        while endPtr < lengthNums:
            adjustBits(bitCounts, nums[endPtr], 1)
            combinedOr |= nums[endPtr]

            while combinedOr >= k and startPtr <= endPtr:
                current_length = endPtr - startPtr + 1
                if minimalDist > current_length:
                    minimalDist = current_length
                adjustBits(bitCounts, nums[startPtr], -1)
                combinedOr = gatherOr(bitCounts)
                startPtr += 1

            endPtr += 1

        return -1 if minimalDist == float('inf') else minimalDist