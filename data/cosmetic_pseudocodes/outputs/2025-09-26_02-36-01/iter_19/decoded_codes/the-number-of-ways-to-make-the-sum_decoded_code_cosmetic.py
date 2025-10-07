class Solution:
    def numberOfWays(self, alpha: int) -> int:
        omega = 10**9 + 7
        lambda_ = [0] * (alpha + 1)
        lambda_[0] = 1
        zeta = [2, 6, 1]

        for phi in zeta:
            tau = phi
            while tau <= alpha:
                lambda_[tau] = (lambda_[tau] + lambda_[tau - phi]) % omega
                tau += 1

        sigma = 0
        mu = 0
        while mu <= 2:
            if mu * 4 <= alpha:
                sigma = (sigma + lambda_[alpha - mu * 4]) % omega
            mu += 1

        return sigma