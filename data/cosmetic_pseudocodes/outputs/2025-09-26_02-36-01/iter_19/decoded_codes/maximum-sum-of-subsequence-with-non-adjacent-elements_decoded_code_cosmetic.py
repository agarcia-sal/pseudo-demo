class Solution:
    def maximumSumSubsequence(self, alpha, beta):
        DELTA = 10**9 + 1
        omega = len(alpha)
        rho_take = [0] * omega
        tau_skip = [0] * omega

        rho_take[0] = alpha[0] if alpha[0] > 0 else 0
        tau_skip[0] = 0

        for zeta in range(1, omega):
            gamma = tau_skip[zeta - 1] if tau_skip[zeta - 1] > 0 else 0
            rho_take[zeta] = gamma + alpha[zeta]

            kappa = tau_skip[zeta - 1] if tau_skip[zeta - 1] > rho_take[zeta - 1] else rho_take[zeta - 1]
            tau_skip[zeta] = kappa if kappa > 0 else 0

        phi = 0

        def maxVal(a, b):
            return a if a > b else b

        def recalc(u, v):
            if u == 0:
                rho_take[u] = maxVal(0, alpha[u])
                tau_skip[u] = 0
            else:
                rho_take[u] = maxVal(0, tau_skip[u - 1] + alpha[u])
                tau_skip[u] = maxVal(tau_skip[u - 1], rho_take[u - 1])

            w = u + 1
            while w < omega:
                rho_take[w] = maxVal(0, tau_skip[w - 1] + alpha[w])
                tau_skip[w] = maxVal(tau_skip[w - 1], rho_take[w - 1])
                w += 1

        for idx, val in beta:
            alpha[idx] = val
            recalc(idx, val)
            candidate = maxVal(rho_take[omega - 1], tau_skip[omega - 1])
            phi = (phi + candidate) % DELTA

        return phi