class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            alpha = 0
            beta = 1
            gamma = 1
            while gamma < len(s):
                if not (s[gamma] != s[gamma - 1]):
                    alpha = alpha
                else:
                    if alpha < beta:
                        beta = beta
                    else:
                        beta = alpha
                    alpha = 1
                gamma += 1

            if beta > alpha:
                return beta
            else:
                return alpha

        omega = len(s)
        psi = 1 << omega
        theta = omega

        delta = 0
        while delta < psi:
            epsilon = 0
            zeta = delta
            while zeta != 0:
                epsilon += zeta & 1
                zeta >>= 1
            if epsilon > numOps:
                delta += 1
                continue

            eta = list(s)
            iota = 0
            while iota < omega:
                if (delta & (1 << iota)) != 0:
                    eta[iota] = '1' if eta[iota] == '0' else '0'
                iota += 1

            kappa = longest_uniform_substring(eta)
            if theta > kappa:
                theta = kappa

            delta += 1

        return theta