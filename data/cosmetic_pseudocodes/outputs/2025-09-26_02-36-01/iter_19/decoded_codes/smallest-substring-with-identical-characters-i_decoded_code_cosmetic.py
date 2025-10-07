class Solution:
    def minLength(self, s, numOps):
        def longest_uniform_substring(s):
            omega = 0
            delta = 1
            lambda_ = 1
            while lambda_ < len(s):
                if s[lambda_] == s[lambda_ - delta]:
                    delta += 1
                else:
                    if omega < delta:
                        omega = delta
                    delta = 1
                lambda_ += 1
            return omega if omega > delta else delta

        def count_bits_set(x):
            acc = 0
            temp = x
            while temp != 0:
                acc += temp & 1
                temp >>= 1
            return acc

        alpha = len(s)
        beta = 1 << len(s)
        kappa = 0
        while kappa < beta:
            if count_bits_set(kappa) > numOps:
                kappa += 1
                continue

            mu = list(s)
            nu = 0
            while nu < len(s):
                if (kappa & (1 << nu)) != 0:
                    mu[nu] = '1' if mu[nu] == '0' else '0'
                nu += 1

            pi = longest_uniform_substring(mu)
            if alpha > pi:
                alpha = pi
            kappa += 1

        return alpha