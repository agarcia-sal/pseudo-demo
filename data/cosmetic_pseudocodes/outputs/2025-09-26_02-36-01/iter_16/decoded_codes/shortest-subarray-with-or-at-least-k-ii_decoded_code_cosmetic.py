class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def update_count(count: list[int], num: int, add: int) -> None:
            bitMask = 1
            idx = 0
            while idx < 32:
                if (num & bitMask) != 0:
                    count[idx] += add
                bitMask <<= 1
                idx += 1

        def compute_current_or(count: list[int]) -> int:
            result = 0
            position = 0
            while position < 32:
                if count[position] > 0:
                    result |= (1 << position)
                position += 1
            return result

        arrayLength = len(nums)
        bitCounts = [0] * 32
        currentValue = 0
        startIndex = 0
        minimalLength = float('inf')

        while startIndex <= arrayLength - 1:
            endIndex = startIndex
            while endIndex < arrayLength:
                update_count(bitCounts, nums[endIndex], 1)
                currentValue |= nums[endIndex]

                if currentValue >= k:
                    curr_length = (endIndex - startIndex) + 1
                    if minimalLength > curr_length:
                        minimalLength = curr_length
                    update_count(bitCounts, nums[startIndex], -1)
                    currentValue = compute_current_or(bitCounts)
                    startIndex += 1
                    break
                endIndex += 1
            if endIndex >= arrayLength:
                break

        return minimalLength if minimalLength != float('inf') else -1