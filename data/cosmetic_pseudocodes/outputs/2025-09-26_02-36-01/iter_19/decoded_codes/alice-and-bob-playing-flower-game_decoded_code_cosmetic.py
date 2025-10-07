class Solution:
    def flowerGame(self, tau, sigma):
        delta = 1
        gamma = 2
        kappa = (tau + delta) / gamma
        lam = tau / gamma  # 'lambda' is a reserved keyword in Python, renamed to 'lam'
        mu = (sigma + delta) / gamma
        nu = sigma / gamma

        def computeProduct(alpha, beta):
            return alpha * beta

        partOne = computeProduct(kappa, nu)
        partTwo = computeProduct(lam, mu)
        omega = partOne + partTwo
        return omega