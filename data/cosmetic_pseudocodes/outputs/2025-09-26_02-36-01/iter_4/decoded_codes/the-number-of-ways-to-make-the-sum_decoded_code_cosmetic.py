class Solution:
    def numberOfWays(self, n: int) -> int:
        modulus = 10**9 + 7
        ways = [0] * (n + 1)
        ways[0] = 1
        coinList = [1, 2, 6]

        for currentCoin in coinList:
            pos = currentCoin
            while pos <= n:
                ways[pos] = (ways[pos] + ways[pos - currentCoin]) % modulus
                pos += 1

        total = 0
        for counter in range(3):
            productVal = counter * 4
            if productVal <= n:
                total = (total + ways[n - productVal]) % modulus

        return total