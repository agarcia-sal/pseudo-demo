from bisect import bisect_left

class Solution:
    def resultArray(self, nums):
        A = [nums[0]]
        B = [nums[1]]
        SA = [nums[0]]
        SB = [nums[1]]

        def count_greater(X, Y):
            # number of elements in X greater than Y using binary search
            l, r = 0, len(X)
            while l < r:
                m = (l + r) // 2
                if Y >= X[m]:
                    l = m + 1
                else:
                    r = m
            return len(X) - l

        idx = 2
        while idx < len(nums):
            v = nums[idx]
            cA = count_greater(SA, v)
            cB = count_greater(SB, v)

            if cA > cB:
                A.append(v)
                p = len(SA)
                l = 0
                while l < p:
                    m = (l + p) // 2
                    if v < SA[m]:
                        p = m
                    else:
                        l = m + 1
                SA.insert(l, v)
            elif cA < cB:
                B.append(v)
                p = len(SB)
                l = 0
                while l < p:
                    m = (l + p) // 2
                    if v < SB[m]:
                        p = m
                    else:
                        l = m + 1
                SB.insert(l, v)
            else:
                if len(A) <= len(B):
                    A.append(v)
                    p = len(SA)
                    l = 0
                    while l < p:
                        m = (l + p) // 2
                        if v < SA[m]:
                            p = m
                        else:
                            l = m + 1
                    SA.insert(l, v)
                else:
                    B.append(v)
                    p = len(SB)
                    l = 0
                    while l < p:
                        m = (l + p) // 2
                        if v < SB[m]:
                            p = m
                        else:
                            l = m + 1
                    SB.insert(l, v)
            idx += 1
        return A + B