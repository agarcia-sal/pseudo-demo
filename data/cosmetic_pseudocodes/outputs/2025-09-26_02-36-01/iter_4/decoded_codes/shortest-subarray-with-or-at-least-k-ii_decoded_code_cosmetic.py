class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def update_count(counter: list[int], value: int, delta: int) -> None:
            bitMask = 1
            idx = 0
            while idx <= 31:
                if (value & bitMask) != 0:
                    counter[idx] += delta
                bitMask <<= 1
                idx += 1

        def compute_current_or(counter: list[int]) -> int:
            res = 0
            position = 0
            while position <= 31:
                if counter[position] > 0:
                    res |= (1 << position)
                position += 1
            return res

        lengthNums = len(nums)
        bitCount = [0] * 32
        accumulatedOr = 0
        startIndex = 0
        shortestLen = float('inf')

        endIndex = 0
        while endIndex < lengthNums:
            update_count(bitCount, nums[endIndex], 1)
            accumulatedOr |= nums[endIndex]

            while accumulatedOr >= k and startIndex <= endIndex:
                currentLen = endIndex - startIndex + 1
                if shortestLen > currentLen:
                    shortestLen = currentLen
                update_count(bitCount, nums[startIndex], -1)
                accumulatedOr = compute_current_or(bitCount)
                startIndex += 1

            endIndex += 1

        return -1 if shortestLen == float('inf') else shortestLen