class Solution:
    def maxScore(self, alpha, beta):
        def isPossible(gamma, beta):
            omega = 0
            sigma = 0
            delta = 0
            epsilon = len(alpha)
            while delta < epsilon:
                point = alpha[delta]
                theta = (gamma + point - 1) // point
                if theta - sigma < 0:
                    theta = 0
                else:
                    theta = theta - sigma
                if theta > 0:
                    omega += (2 * theta - 1)
                    sigma = theta - 1
                else:
                    if delta + 1 < epsilon:
                        omega += 1
                        sigma = 0
                if omega > beta:
                    return False
                delta += 1
            return True

        psi = 0
        chi = ((beta + 1) // 2) * (alpha[0] + 1)
        while psi < chi:
            mu = (psi + chi + 1) // 2
            if isPossible(mu, beta):
                psi = mu
            else:
                chi = mu - 1
        return psi