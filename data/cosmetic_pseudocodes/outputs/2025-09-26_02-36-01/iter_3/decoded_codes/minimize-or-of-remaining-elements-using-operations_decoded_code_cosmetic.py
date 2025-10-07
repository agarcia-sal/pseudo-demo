class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        def canAchieve(expectation: int) -> bool:
            accumulator = -1
            count = 0
            index = 0
            length = len(nums)
            while index < length:
                element = nums[index]
                if accumulator == -1:
                    accumulator = element
                else:
                    accumulator &= element
                if (accumulator & expectation) == 0:
                    accumulator = -1
                else:
                    count += 1
                    if count > k:
                        return False
                index += 1
            return True

        limit = (1 << 30) - 1
        candidate = limit
        position = 0
        while position < 30:
            mask = 1 << position
            if (candidate & mask) == 0:
                position += 1
                continue
            if canAchieve((~candidate) ^ mask):
                candidate &= ~mask
            position += 1
        return candidate