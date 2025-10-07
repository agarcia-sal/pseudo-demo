class Solution:
    def minOrAfterOperations(self, nums: list[int], k: int) -> int:
        def canAchieve(p: int, q: int) -> bool:
            r = -1
            s = 0

            def process_index(u: int) -> bool:
                nonlocal r, s
                if u >= len(nums):
                    return True
                v = nums[u]
                if r == -1:
                    r = v
                else:
                    r &= v
                if (r & p) == 0:
                    r = -1
                else:
                    s += 1
                    if s > q:
                        return False
                return process_index(u + 1)

            return process_index(0)

        w = (1 << 30) - 1
        x = w
        y = 0

        while y <= 29:
            z = 1 << y
            if (x & z) != 0:
                aa = canAchieve((~x) ^ z, k)
                if aa:
                    x &= ~z
            y += 1

        return x