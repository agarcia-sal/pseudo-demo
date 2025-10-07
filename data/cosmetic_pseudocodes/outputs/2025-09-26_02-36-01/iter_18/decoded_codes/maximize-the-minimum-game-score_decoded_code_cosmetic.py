class Solution:
    def maxScore(self, points, m):
        def isPossible(minVal, m):
            alpha = 0
            beta = 0
            k = 0
            n = len(points)
            while k < n:
                phi = (minVal + points[k] - 1) // points[k]
                if (phi - beta) < 0:
                    phi = 0
                else:
                    phi = phi - beta
                if phi > 0:
                    alpha += (2 * phi) - 1
                    beta = phi - 1
                elif (k + 1) < n:
                    alpha += 1
                    beta = 0
                if alpha > m:
                    return False
                k += 1
            return True

        omega = 0
        psi = ((m + 1) // 2) * (points[0] + 1)
        while omega < psi:
            gamma = (omega + psi + 1) // 2
            if isPossible(gamma, m):
                omega = gamma
            else:
                psi = gamma - 1

        return omega