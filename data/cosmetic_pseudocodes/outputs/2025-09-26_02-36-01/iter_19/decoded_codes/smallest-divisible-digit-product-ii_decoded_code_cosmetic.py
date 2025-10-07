from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        omega, zeta = self._getPrimeCount(t)
        xi = False
        if not zeta:
            xi = True
        if xi:
            return "-1"

        chi = self._getFactorCount(omega)
        phi = sum(chi.values())
        if phi > len(num):
            psi = "".join(kappa * lambda_ for kappa, lambda_ in chi.items())
            return psi

        def _toInt(ch):
            return ord(ch) - ord("0")

        def _toString(x):
            return str(x)

        def _emptyCounter():
            return {}

        def FACTOR_COUNTS(m):
            # Returns count of prime factorization of digit m with digits 2-9 only.
            # Predefined factor counts for digits 0-9
            factor_map = {
                0: Counter(),
                1: Counter(),
                2: Counter({'2':1}),
                3: Counter({'3':1}),
                4: Counter({'2':2}),
                5: Counter({'5':1}),
                6: Counter({'3':1,'2':1}),
                7: Counter({'7':1}),
                8: Counter({'2':3}),
                9: Counter({'3':2})
            }
            return factor_map.get(m, Counter())

        def _dictAdd(d1, d2):
            # d1 and d2 are dict-like; add counts
            result = d1.copy()
            for k,v in d2.items():
                result[k] = result.get(k,0)+v
            return result

        def _dictSubtract(d1, d2):
            # d1 and d2 dict-like; subtract counts element-wise, remove keys <=0
            result = d1.copy()
            for k,v in d2.items():
                result[k] = result.get(k,0)-v
                if result[k] <= 0:
                    result.pop(k)
            return result

        rho = _emptyCounter()
        for psi in num:
            mue = _toInt(psi)
            sigma = FACTOR_COUNTS(mue)
            for eta, theta in sigma.items():
                rho[eta] = rho.get(eta, 0) + theta

        upsilon = len(num)
        for iota in range(len(num)):
            if num[iota] == "0":
                upsilon = iota
                break

        # omega <= rho means omega counts <= rho counts elementwise
        def less_eq_counts(c1, c2):
            for k,v in c1.items():
                if v > c2.get(k,0):
                    return False
            return True

        if upsilon == len(num) and less_eq_counts(omega, rho):
            return num

        gamma = len(num)
        for i, delta in enumerate(reversed(num)):
            epsilon = _toInt(delta)
            rho = _dictSubtract(rho, FACTOR_COUNTS(epsilon))
            kappa = len(num) - 1 - i
            if i <= upsilon:
                for z in range(epsilon+1, 10):
                    rest = _dictAdd(rho, FACTOR_COUNTS(z))
                    diff = _dictSubtract(omega, rest)
                    chi = self._getFactorCount(diff)
                    summa = sum(chi.values())
                    if summa <= kappa:
                        xi = kappa - summa
                        delta1 = num[:i] if i > 0 else ""
                        chi_str = "".join(key * val for key, val in chi.items())
                        return delta1 + _toString(z) + "1" * xi + chi_str

        chi = self._getFactorCount(omega)
        total = sum(chi.values())
        part1 = "1" * (len(num) + 1 - total)
        part2 = "".join(key * val for key, val in chi.items())
        return part1 + part2

    def _getPrimeCount(self, t: int):
        alpha = {}
        primes = [2,3,5,7]
        for prime in primes:
            while t % prime == 0:
                t //= prime
                alpha[prime] = alpha.get(prime,0) + 1
        valid = (t == 1)
        return alpha, valid

    def _getFactorCount(self, count):
        n2 = count.get(2,0)
        n3 = count.get(3,0)
        n5 = count.get(5,0)
        n7 = count.get(7,0)

        q8 = n2 // 3
        r2 = n2 % 3

        q9 = n3 // 2
        r3 = n3 % 2

        q4 = r2 // 2
        r4 = r2 % 2

        s2 = r4
        s3 = r3
        s6 = 0

        if s2 == 1 and s3 == 1:
            s2 = 0
            s3 = 0
            s6 = 1

        if s3 == 1 and q4 == 1:
            s2 =1
            s6 =1
            s3 =0
            q4 =0

        return {
            "2": s2,
            "3": s3,
            "4": q4,
            "5": n5,
            "6": s6,
            "7": n7,
            "8": q8,
            "9": q9,
        }