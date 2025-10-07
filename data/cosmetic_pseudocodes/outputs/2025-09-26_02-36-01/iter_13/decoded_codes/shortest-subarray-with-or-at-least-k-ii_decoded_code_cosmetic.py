class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def modifyCounter(counter: list[int], val: int, delta: int):
            def helper(bitPos: int):
                if bitPos == 32:
                    return
                valBit = val & (1 << bitPos)
                if valBit != 0:
                    counter[bitPos] += delta
                helper(bitPos + 1)
            helper(0)

        def aggregateOr(counter: list[int]) -> int:
            accumulator = 0
            for index in range(32):
                if counter[index] > 0:
                    accumulator |= (1 << index)
            return accumulator

        arraySize = len(nums)

        bitCount = [0] * 32
        windowStart = 0
        combinedOr = 0
        minSlice = 9999999999999  # Large number for initialization
        indexRunner = 0

        while indexRunner < arraySize:
            modifyCounter(bitCount, nums[indexRunner], 1)
            combinedOr |= nums[indexRunner]
            while combinedOr >= k and windowStart <= indexRunner:
                current_length = indexRunner - windowStart + 1
                if minSlice > current_length:
                    minSlice = current_length
                modifyCounter(bitCount, nums[windowStart], -1)
                combinedOr = aggregateOr(bitCount)
                windowStart += 1
            indexRunner += 1

        return -1 if minSlice == 9999999999999 else minSlice