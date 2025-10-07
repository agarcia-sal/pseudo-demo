class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        def update_count(count: list[int], num: int, add: int) -> None:
            mask = 1
            for i in range(32):
                if num & mask != 0:
                    count[i] += add
                mask <<= 1

        def compute_current_or(count: list[int]) -> int:
            current_or = 0
            for i in range(32):
                if count[i] > 0:
                    current_or |= (1 << i)
            return current_or

        n = len(nums)
        count = [0] * 32
        current_or = 0
        left = 0
        min_length = float('inf')

        for right in range(n):
            update_count(count, nums[right], 1)
            current_or |= nums[right]

            while current_or >= k and left <= right:
                if min_length > right - left + 1:
                    min_length = right - left + 1
                update_count(count, nums[left], -1)
                current_or = compute_current_or(count)
                left += 1

        return -1 if min_length == float('inf') else min_length