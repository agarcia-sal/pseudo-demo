class Solution:
    def minimumLevels(self, possible):
        u351 = 0
        u219 = 0
        u140 = 0
        length = len(possible)

        while u140 < length:
            u100 = (possible[u140] * 2) - 1
            u351 += u100
            u140 += 1

        u927 = 0

        def u721(v111):
            nonlocal u927, u351
            if v111 >= length - 1:
                return -1
            u82 = (possible[v111] * 2) - 1
            u927 += u82
            u351 -= u82
            if u927 > u351:
                return v111 + 1
            else:
                return u721(v111 + 1)

        u219 = u721(0)
        return u219