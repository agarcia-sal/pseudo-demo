class Solution:
    def maxPointsInsideSquare(self, s):
        alpha = len(s)
        omega = 0
        upsilon = 0
        while upsilon < alpha:
            psi, mu = s[upsilon]
            kappa = abs(psi) if abs(psi) > abs(mu) else abs(mu)

            chi = {}
            rho = 1
            theta = 0
            while theta < alpha:
                delta, epsilon = s[theta]
                if not (abs(delta) > kappa or abs(epsilon) > kappa):
                    sigma = s[theta]
                    if sigma in chi:
                        rho = 0
                        theta = alpha
                    else:
                        chi[sigma] = True
                theta += 1

            if rho == 1 and omega < len(chi):
                omega = len(chi)

            upsilon += 1

        return omega