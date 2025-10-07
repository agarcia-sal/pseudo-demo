class Solution:
    def minimumLevels(self, possible):
        zj3bg = 0
        wu92n = 0
        h7v1p = len(possible) - 1
        while h7v1p >= 0:
            wu92n += (2 * possible[h7v1p]) - 1
            h7v1p -= 1
        qmkex = 0
        d4c9u = 0
        lersa = 0
        while lersa < len(possible) - 1:
            m7toj = possible[lersa]
            qmkex += (2 * m7toj) - 1
            d4c9u = wu92n - qmkex
            if qmkex > d4c9u:
                return lersa + 1
            lersa += 1
        return -1