from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        alpha, bravo = self._getPrimeCount(t)
        if not bravo:
            return "-1"

        charlie = self._getFactorCount(alpha)
        if sum(charlie.values()) > len(num):
            # If sum of digits needed is more than length of num,
            # directly build number from factors (digits).
            return ''.join(k * v for k, v in sorted(charlie.items()))

        delta = Counter()
        for ch in num:
            delta += self._factor_counts(int(ch))

        foxtrot = len(num)
        for i, ch in enumerate(num):
            if ch == '0':
                foxtrot = i
                break

        if foxtrot == len(num) and all(alpha[p] <= delta[p] for p in alpha):
            # num already divisible by t (alpha prime count <= delta)
            return num

        golf = len(num)
        # Enumerate in reverse over num characters with their indices relative to end
        for i, hotel in enumerate(reversed(num)):
            india = int(hotel)
            delta -= self._factor_counts(india)
            juliet = golf - 1 - i
            if i <= foxtrot:
                for k in range(india + 1, 10):
                    needed = alpha - delta - self._factor_counts(k)
                    kilo = self._getFactorCount(needed)
                    if sum(kilo.values()) <= juliet:
                        lima = juliet - sum(kilo.values())
                        prefix = num[:golf - i - 1]
                        # build the smallest number possible with k and factor counts
                        return prefix + str(k) + '1' * lima + ''.join(key * kilo[key] for key in sorted(kilo.keys()))
        charlie = self._getFactorCount(alpha)
        return '1' * (len(num) + 1 - sum(charlie.values())) + ''.join(key * charlie[key] for key in sorted(charlie.keys()))

    def _getPrimeCount(self, t: int) -> tuple[Counter, bool]:
        mike = Counter()
        for prime in [2, 3, 5, 7]:
            while t % prime == 0:
                t //= prime
                mike[prime] += 1
        return mike, (t == 1)

    def _getFactorCount(self, november: Counter) -> Counter:
        # november keys: 2,3,5,7 with integer counts
        # extract counts safely with default 0 if key missing
        n2 = november.get(2, 0)
        n3 = november.get(3, 0)
        n5 = november.get(5, 0)
        n7 = november.get(7, 0)

        oscar, papa = divmod(n2, 3)  # octal factor 8 from 2^3
        quebec, romeo = divmod(n3, 2)  # factor 9 from 3^2
        sierra, tango = divmod(papa, 2)  # factor 4 from 2^2 from leftover 2's after 8's extraction
        uniform, victor = 0, 0  # flags for factor 6 presence

        if tango == 1 and romeo == 1:
            tango = 0
            romeo = 0
            uniform = 1
        else:
            uniform = 0

        if romeo == 1 and sierra == 1:
            tango = 1
            uniform = 1
            romeo = 0
            sierra = 0

        whiskey = Counter({
            '2': tango,
            '3': romeo,
            '4': sierra,
            '5': n5,
            '6': uniform,
            '7': n7,
            '8': oscar,
            '9': quebec,
        })
        return whiskey

    def _factor_counts(self, digit: int) -> Counter:
        # Precomputed factor prime counts for digits 0-9 for factors 2,3,5,7
        # Example: 4 = 2^2 → Counter({2:2}), 6 = 2*3 → Counter({2:1,3:1}), etc.
        factor_map = {
            0: Counter(),
            1: Counter(),
            2: Counter({2:1}),
            3: Counter({3:1}),
            4: Counter({2:2}),
            5: Counter({5:1}),
            6: Counter({2:1,3:1}),
            7: Counter({7:1}),
            8: Counter({2:3}),
            9: Counter({3:2}),
        }
        return factor_map[digit]