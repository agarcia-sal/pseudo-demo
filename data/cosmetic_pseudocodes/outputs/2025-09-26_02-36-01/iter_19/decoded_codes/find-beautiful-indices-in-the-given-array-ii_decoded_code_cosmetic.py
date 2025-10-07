class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        omega = []
        gamma = len(s) - len(a)
        delta = 0
        while delta <= gamma:
            epsilon = ""
            zeta = 0
            while zeta < len(a):
                epsilon += s[delta + zeta]
                zeta += 1
            if epsilon == a:
                omega.append(delta)
            delta += 1

        eta = []
        theta = len(s) - len(b)
        iota = 0
        while True:
            if iota > theta:
                break
            kappa = ""
            lambda_ = 0
            while lambda_ < len(b):
                kappa += s[iota + lambda_]
                lambda_ += 1
            if kappa == b:
                eta.append(iota)
            iota += 1

        mu = []
        alpha = 0
        beta = 0
        while True:
            if not (alpha < len(omega) and beta < len(eta)):
                break
            tau = omega[alpha] - eta[beta]
            if tau < 0:
                tau = -tau
            if tau <= k:
                mu.append(omega[alpha])
                alpha += 1
            else:
                if omega[alpha] < eta[beta]:
                    alpha += 1
                else:
                    beta += 1

        return mu