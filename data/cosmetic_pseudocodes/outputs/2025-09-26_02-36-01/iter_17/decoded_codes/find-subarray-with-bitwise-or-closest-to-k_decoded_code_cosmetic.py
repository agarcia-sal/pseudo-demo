class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        length = len(nums)
        minimal_gap = float('inf')

        for a in range(length):
            running_or = 0
            for b in range(a, length):
                running_or |= nums[b]
                gap = abs(k - running_or)
                if gap < minimal_gap:
                    minimal_gap = gap
                if gap == 0:
                    return 0
        return minimal_gap