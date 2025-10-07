from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        def custom_maximum(arr):
            p = arr[0]
            q = 1
            while q < len(arr):
                if arr[q] > p:
                    p = arr[q]
                q += 1
            return p

        def insert_into_dict(dct, key, val):
            if key not in dct:
                dct[key] = []
            dct[key].append(val)

        alpha = {}
        beta = 0

        idx1 = 0
        while idx1 < len(nums):
            insert_into_dict(alpha, nums[idx1], idx1)
            idx1 += 1

        for gamma in alpha.values():
            n = len(gamma)

            def inner_loop(x):
                nonlocal beta
                if x >= n:
                    return
                def inner_j(y):
                    nonlocal beta
                    if y >= n:
                        return
                    delta = []
                    zeta = gamma[x]
                    eta = gamma[y]
                    k = zeta
                    while k <= eta:
                        delta.append(nums[k])
                        k += 1
                    if custom_maximum(delta) == nums[zeta]:
                        beta += 1
                    inner_j(y + 1)
                inner_j(x)
                inner_loop(x + 1)

            inner_loop(0)

        return beta