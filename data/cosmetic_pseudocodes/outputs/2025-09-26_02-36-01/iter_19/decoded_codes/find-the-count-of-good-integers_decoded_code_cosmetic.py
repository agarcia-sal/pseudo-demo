class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        omega = []
        theta = set()
        lambda_val = 10 ** ((n - 1) // 2)

        def sigma(z: int) -> int:
            if z <= 1:
                return 1
            else:
                return z * sigma(z - 1)

        # Precompute factorials 0 through n
        delta = 0
        while delta <= n:
            omega.append(sigma(delta))
            delta += 1

        def chi(text: str) -> dict:
            eta = {}
            psi = 0
            while psi < len(text):
                alpha = text[psi]
                eta[alpha] = eta.get(alpha, 0) + 1
                psi += 1
            return eta

        phi = 0
        iota = lambda_val
        upper_limit = lambda_val * 10 - 1
        n_mod_2 = n % 2

        while iota <= upper_limit:
            rho = str(iota)
            upsilon = ""
            pi = len(rho) - 1
            while pi >= n_mod_2:
                upsilon += rho[pi]
                pi -= 1
            rho = rho + upsilon

            if int(rho) % k != 0:
                iota += 1
                continue

            kappa = ''.join(sorted(rho))
            if kappa in theta:
                iota += 1
                continue

            theta.add(kappa)
            mu = chi(kappa)
            if '0' in mu and mu['0'] > 0:
                nu = (n - mu['0']) * omega[n - 1]
            else:
                nu = omega[n]

            for val in mu.values():
                nu //= omega[val]

            phi += nu
            iota += 1

        return phi