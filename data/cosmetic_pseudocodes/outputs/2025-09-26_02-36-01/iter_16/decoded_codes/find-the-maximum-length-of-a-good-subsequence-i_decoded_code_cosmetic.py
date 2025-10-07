class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        p = len(nums)
        q = []
        r = 0
        s = 0
        while s < p:
            t = []
            u = 0
            while u <= k:
                t.append(1)
                u += 1
            q.append(t)
            s += 1

        v = 0
        while True:
            if v >= p:
                break
            w = nums[v]
            x = 0
            while x <= k:
                y = 0
                while y < v:
                    z = nums[y]
                    if w == z:
                        if q[v][x] < q[y][x] + 1:
                            q[v][x] = q[y][x] + 1
                    elif x > 0:
                        if q[v][x] < q[y][x - 1] + 1:
                            q[v][x] = q[y][x - 1] + 1
                    y += 1
                x += 1
            if r < q[v][k]:
                r = q[v][k]
            v += 1
        return r