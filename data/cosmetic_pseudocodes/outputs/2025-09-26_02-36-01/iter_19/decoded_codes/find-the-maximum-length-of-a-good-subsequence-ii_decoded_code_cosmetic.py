from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        q = len(nums)
        l = [[0] * (k + 1) for _ in range(q)]
        r = [defaultdict(int) for _ in range(k + 1)]
        s = [[0, 0, 0] for _ in range(k + 1)]
        w = 0
        a = 0
        while a < q:
            b = nums[a]
            c = 0
            while c <= k:
                l[a][c] = r[c][b]
                if c > 0:
                    if s[c - 1][0] != nums[a]:
                        l[a][c] = max(l[a][c], s[c - 1][1])
                    else:
                        l[a][c] = max(l[a][c], s[c - 1][2])
                l[a][c] += 1
                r[c][nums[a]] = max(r[c][nums[a]], l[a][c])
                if s[c][0] != b:
                    if l[a][c] >= s[c][1]:
                        s[c][2] = s[c][1]
                        s[c][1] = l[a][c]
                        s[c][0] = b
                    else:
                        s[c][2] = max(s[c][2], l[a][c])
                else:
                    s[c][1] = max(s[c][1], l[a][c])
                w = max(w, l[a][c])
                c += 1
            a += 1
        return w