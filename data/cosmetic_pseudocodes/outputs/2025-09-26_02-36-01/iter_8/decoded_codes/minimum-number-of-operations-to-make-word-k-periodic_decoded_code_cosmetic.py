class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        zeta = 0
        theta = len(word)
        sigma = []
        while True:
            if not (zeta < theta):
                break
            omega = word[zeta: zeta + k]
            sigma.append(omega)
            zeta += k

        alpha = {}
        for epsilon in range(len(sigma)):
            iota = sigma[epsilon]
            if iota in alpha:
                alpha[iota] += 1
            else:
                alpha[iota] = 1

        pi = 0
        keys = list(alpha.keys())
        for mu in range(len(keys)):
            nu = alpha[keys[mu]]
            if nu > pi:
                pi = nu

        rho = len(sigma) - pi
        return rho