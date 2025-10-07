class Solution:
    def countDays(self, omega: int, psi: list[list[int]]) -> int:
        def customSort(zeta: list[list[int]]) -> None:
            n = len(zeta)
            for alpha in range(1, n):
                for beta in range(1, n - alpha):
                    # adjust indices for 0-based Python lists
                    if zeta[beta][1] > zeta[beta + 1][1]:
                        zeta[beta], zeta[beta + 1] = zeta[beta + 1], zeta[beta]

        # customSort uses 1-based indices from pseudocode; translate carefully
        # However, Python uses 0-based indexing; we must adapt the loops:
        # The pseudocode loops alpha from 1 to length(zeta)-1 inclusive,
        # beta from 1 to length(zeta)-alpha inclusive.
        # Indices inside zeta[beta][1] correspond to zero-based beta-1 and beta.
        # We rewrite the customSort with 0-based indexing accordingly.

        def customSort(zeta: list[list[int]]) -> None:
            n = len(zeta)
            for alpha in range(1, n):
                for beta in range(0, n - alpha):
                    if zeta[beta][1] > zeta[beta + 1][1]:
                        zeta[beta], zeta[beta + 1] = zeta[beta + 1], zeta[beta]

        customSort(psi)
        lam = 1
        sigma = 0

        def processMeetings(index: int, tau: int, upsilon: int) -> int:
            if index > len(psi):
                return upsilon
            pi = psi[index - 1][0]  # psi[index][1] in 1-based; here index-1 and 0 (start time)
            rho = psi[index - 1][1] # psi[index][2] in 1-based; here index-1 and 1 (end time)
            if tau < pi:
                sigma_ = upsilon + (pi - tau)
            else:
                sigma_ = upsilon
            tau_new = max(tau, rho) + 1
            return processMeetings(index + 1, tau_new, sigma_)

        sigma = processMeetings(1, lam, sigma)
        if lam <= omega:
            sigma += omega - lam + 1
        return sigma