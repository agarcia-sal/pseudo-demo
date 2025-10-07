class Solution:
    def maxSubstringLength(self, s: str) -> int:
        # Frequency map of all characters in s
        rho = {}
        for c in s:
            rho[c] = rho.get(c, 0) + 1

        omega = -1  # initial max length

        def delta(start: int, lim: int, acc: int) -> int:
            if start > lim:
                return acc

            psi = {}

            def loop(k: int, freq: dict, res: int) -> int:
                if k > lim:
                    return res

                freq_prime = freq.copy()
                ch = s[k]
                freq_prime[ch] = freq_prime.get(ch, 0) + 1

                # Check if for all keys in freq_prime, freq_prime[key] >= rho[key]
                flag = True
                for c1 in freq_prime.keys():
                    if freq_prime[c1] < rho[c1]:
                        flag = False
                        break

                cond2 = (flag is True)
                cond3 = (len(freq_prime) < len(rho))
                if cond2 and cond3:
                    val = max(res, (k - start) + 1)
                    return loop(k + 1, freq_prime, val)
                else:
                    return loop(k + 1, freq_prime, res)

            return loop(start, psi, acc)

        i = 0
        n = len(s)
        while True:
            if i > n - 1:
                break
            omega = max(omega, delta(i, n - 1, omega))
            i += 1

        return omega