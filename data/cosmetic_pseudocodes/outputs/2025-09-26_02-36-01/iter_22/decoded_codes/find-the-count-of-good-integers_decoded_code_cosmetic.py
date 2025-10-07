from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        gamma = []

        def computeFactorials(limit: int):
            zeta = 1
            y = 0
            while y < limit:
                gamma.append(zeta)
                zeta *= (y + 1)
                y += 1

        computeFactorials(n + 1)

        delta = 0
        epsilon = set()

        omega = 10
        alpha = 1
        beta = n - 1

        iota = omega ** ((n - 1) // 2)
        lambda_ = iota * omega

        mu = iota

        while mu < lambda_:
            sigma = str(mu)
            varkappa = len(sigma)
            rho = n % 2

            # psi is a substring of reversed sigma, starting at index rho, length varkappa - rho
            reversed_sigma = sigma[::-1]
            psi = reversed_sigma[rho : varkappa - rho]

            chi = sigma + psi
            nu = int(chi)

            if nu % k != 0:
                mu += 1
                continue

            upsilon = list(chi)
            upsilon.sort()
            phi = ''.join(upsilon)

            if phi in epsilon:
                mu += 1
                continue

            epsilon.add(phi)

            tally = Counter(phi)

            if '0' in tally and tally['0'] > 0:
                res = (n - tally['0']) * gamma[n - 1]
            else:
                res = gamma[n]

            for val in tally.values():
                res //= gamma[val]

            delta += res
            mu += 1

        return delta