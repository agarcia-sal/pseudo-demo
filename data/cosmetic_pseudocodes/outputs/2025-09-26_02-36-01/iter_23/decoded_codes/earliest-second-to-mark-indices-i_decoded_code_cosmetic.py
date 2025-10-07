from math import floor

class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        u1 = len(nums)
        u2 = len(changeIndices)

        def can_mark_by_second(u3):
            u4 = [-1] * u1

            def recurse_u5(u6):
                if u6 == u3:
                    return
                u7 = changeIndices[u6] - 1
                u4[u7] = u6
                recurse_u5(u6 + 1)
            recurse_u5(0)

            u8 = 0
            for u9 in range(u1):
                u8 += nums[u9]

            u10 = 0
            u11 = set()

            def recurse_u12(u13):
                nonlocal u10
                if u13 == u3:
                    return
                u14 = changeIndices[u13] - 1
                if u14 not in u11:
                    if u4[u14] == u13:
                        if nums[u14] <= u10:
                            u10 -= nums[u14]
                            u11.add(u14)
                        else:
                            nonlocal u15
                            u15 = False
                            return
                    else:
                        u10 += 1
                else:
                    u10 += 1
                recurse_u12(u13 + 1)

            u15 = True
            recurse_u12(0)
            return (len(u11) == u1) and u15

        u16 = 0
        u17 = u2 + 1
        while u16 < u17:
            u18 = floor((u16 + u17) / 2)
            if can_mark_by_second(u18):
                u17 = u18
            else:
                u16 += 1

        if u16 <= u2:
            return u16
        else:
            return -1