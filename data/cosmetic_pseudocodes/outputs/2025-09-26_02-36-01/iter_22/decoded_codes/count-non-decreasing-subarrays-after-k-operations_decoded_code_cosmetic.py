class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        m = len(nums)

        def canMakeNonDecreasing(p: int, q: int) -> bool:
            u = 0
            v = nums[p]
            w = 1
            while w < q:
                if nums[p + w] < v:
                    u += v - nums[p + w]
                if v < nums[p + w]:
                    v = nums[p + w]
                if u > k:
                    return False
                w += 1
            return True

        total_subarrays = m * (m + 1) // 2
        r = 0
        s = 0
        while s <= m - 1:
            a, b = 1, m - s
            while a <= b:
                c = (a + b) // 2
                if canMakeNonDecreasing(s, c):
                    a = c + 1
                else:
                    b = c - 1
            r += (m - s - b)
            s += 1

        return total_subarrays - r