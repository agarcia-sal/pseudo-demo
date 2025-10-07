class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def modifyCounter(counter: list[int], val: int, delta: int) -> None:
            bitMask = 1
            idx = 0
            while idx < 32:
                if val & bitMask != 0:
                    counter[idx] += delta
                bitMask <<= 1
                idx += 1

        def deriveOr(counter: list[int]) -> int:
            accOr = 0
            pos = 0
            while pos < 32:
                if counter[pos] > 0:
                    accOr |= (1 << pos)
                pos += 1
            return accOr

        length = len(nums)
        bitCounter = [0] * 32
        cumulativeOr = 0
        start = 0
        bestLength = float('inf')

        for pointer in range(length):
            modifyCounter(bitCounter, nums[pointer], 1)
            cumulativeOr |= nums[pointer]

            while cumulativeOr >= k and start <= pointer:
                currentLength = pointer - start + 1
                if bestLength > currentLength:
                    bestLength = currentLength
                modifyCounter(bitCounter, nums[start], -1)
                cumulativeOr = deriveOr(bitCounter)
                start += 1

        return -1 if bestLength == float('inf') else bestLength