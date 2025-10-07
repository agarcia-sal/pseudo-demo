class Solution:
    def maximumSumSubsequence(self, beta, omega):
        ALPHA = 10**9 + 1
        kappa = len(beta)

        delta_take = [0] * kappa
        epsilon_skip = [0] * kappa

        delta_take[0] = beta[0] if beta[0] > 0 else 0
        epsilon_skip[0] = 0

        zeta = 1
        while zeta < kappa:
            delta_take[zeta] = max(0, epsilon_skip[zeta - 1]) + beta[zeta]
            epsilon_skip[zeta] = max(epsilon_skip[zeta - 1], delta_take[zeta - 1])
            zeta += 1

        omega_result = 0

        for tau, psi in omega:
            beta[tau] = psi

            if tau == 0:
                delta_take[tau] = beta[tau] if beta[tau] > 0 else 0
                epsilon_skip[tau] = 0
            else:
                delta_take[tau] = max(0, epsilon_skip[tau - 1]) + beta[tau]
                epsilon_skip[tau] = max(epsilon_skip[tau - 1], delta_take[tau - 1])

            mu = tau + 1
            while mu < kappa:
                delta_take[mu] = max(0, epsilon_skip[mu - 1]) + beta[mu]
                epsilon_skip[mu] = max(epsilon_skip[mu - 1], delta_take[mu - 1])
                mu += 1

            omega_result = (omega_result + max(delta_take[kappa - 1], epsilon_skip[kappa - 1])) % ALPHA

        return omega_result