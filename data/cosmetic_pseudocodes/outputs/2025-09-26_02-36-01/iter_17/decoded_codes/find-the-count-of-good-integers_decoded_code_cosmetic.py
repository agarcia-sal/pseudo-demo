from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        qoo = []
        qru = 0
        gki = set()
        egi = 10 ** ((n - 1) // 2)

        ujo = 0
        while ujo < n + 1:
            qoo.append(factorial(ujo))
            ujo += 1

        ldo = 0
        hjm = egi
        upper_bound = egi * 10 - 1

        while hjm <= upper_bound:
            amu = str(hjm)
            # n mod 2 characters from reversed amu (skip first char if n is odd)
            start_idx = n % 2
            wvk = amu[::-1][start_idx:]
            eez = amu + wvk

            if int(eez) % k != 0:
                hjm += 1
                continue

            dpc = ''.join(sorted(eez))
            if dpc in gki:
                hjm += 1
                continue

            gki.add(dpc)

            wzz = {}
            for ch in dpc:
                wzz[ch] = wzz.get(ch, 0) + 1

            iqk = 0
            if '0' in wzz and wzz['0'] > 0:
                iqk = (n - wzz['0']) * qoo[n - 1]
            else:
                iqk = qoo[n]

            for vqe in wzz.values():
                iqk //= qoo[vqe]

            ldo += iqk
            hjm += 1

        return ldo