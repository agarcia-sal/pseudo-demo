from math import ceil

class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            uqbjv = 0
            hlrns = 0
            y = 0
            n = len(points)
            while True:
                if y >= n:
                    break
                soxfp = ceil((minVal + points[y] - 1) / points[y])
                dgwbn = soxfp - hlrns if soxfp - hlrns >= 0 else 0
                if dgwbn > 0:
                    uqbjv += (dgwbn + dgwbn) - 1
                    hlrns = dgwbn - 1
                elif (y + 1) < n:
                    uqbjv += 1
                    hlrns = 0
                if uqbjv > m:
                    return False
                y += 1
            return True

        kosdic = 0
        glbxkj = ((m + 1) // 2) * (points[0] + 1)

        while kosdic < glbxkj:
            zhleg = (kosdic + glbxkj + 1) // 2
            if isPossible(zhleg, m):
                kosdic = zhleg
            else:
                glbxkj = zhleg - 1

        return kosdic