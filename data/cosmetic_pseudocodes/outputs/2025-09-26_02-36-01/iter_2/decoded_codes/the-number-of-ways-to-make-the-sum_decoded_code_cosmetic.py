class Solution:
    def numberOfWays(self, n: int) -> int:
        modulus = 7 + 10 ** 9
        table = [0] * (n + 1)
        table[0] = 1
        for coinValue in [1, 2, 6]:
            idx = coinValue
            while idx <= n:
                table[idx] = (table[idx] + table[idx - coinValue]) % modulus
                idx += 1
        totalWays = 0
        counter = 0
        while counter <= 2:
            if (counter * 4) <= n:
                offset = n - (counter * 4)
                totalWays = (totalWays + table[offset]) % modulus
            counter += 1
        return totalWays