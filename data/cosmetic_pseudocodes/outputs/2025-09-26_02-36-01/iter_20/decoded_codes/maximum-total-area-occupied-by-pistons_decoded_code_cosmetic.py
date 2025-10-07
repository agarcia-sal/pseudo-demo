class Solution:
    def maxArea(self, height, positions, directions):
        def charUp():
            return 'U'

        def charDown():
            return 'D'

        def strConcat(a, b, c):
            return a + b + c

        def strSub(s, startIndex, endIndex):
            ss = ''
            xx = startIndex
            while xx <= endIndex:
                ss += s[xx]
                xx += 1
            return ss

        alpha = len(positions)
        max_area = 0

        for _ in range(height * 2):
            zeta = 0
            while zeta < alpha:
                if positions[zeta] == 0:
                    if directions[zeta] == charDown():
                        directions = strConcat(strSub(directions, 0, zeta - 1) if zeta > 0 else '',
                                              charUp(),
                                              strSub(directions, zeta + 1, len(directions) - 1) if zeta + 1 <= len(directions) - 1 else '')
                elif positions[zeta] == height:
                    if directions[zeta] == charUp():
                        directions = strConcat(strSub(directions, 0, zeta - 1) if zeta > 0 else '',
                                              charDown(),
                                              strSub(directions, zeta + 1, len(directions) - 1) if zeta + 1 <= len(directions) - 1 else '')

                if directions[zeta] == charUp():
                    positions[zeta] += 1
                else:
                    positions[zeta] -= 1
                zeta += 1

            beta = 0
            idx = 0
            while idx < alpha:
                beta += positions[idx]
                idx += 1

            if max_area < beta:
                max_area = beta

        return max_area