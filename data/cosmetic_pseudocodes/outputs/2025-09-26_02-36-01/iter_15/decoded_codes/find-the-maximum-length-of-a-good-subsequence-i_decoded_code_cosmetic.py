class Solution:
    def maximumLength(self, nums, k):
        q = len(nums)
        r = [[1] * (k + 1) for _ in range(q)]
        s = 0
        p = 0
        while p < q:
            w = nums[p]
            x = 0
            while x <= k:
                y = p - 1
                while y >= 0:
                    z = nums[y]
                    if w == z:
                        r[p][x] = max(r[p][x], r[y][x] + 1)
                    else:
                        if x > 0:
                            r[p][x] = max(r[p][x], r[y][x - 1] + 1)
                    y -= 1
                x += 1
            if s < r[p][k]:
                s = r[p][k]
            p += 1
        return s