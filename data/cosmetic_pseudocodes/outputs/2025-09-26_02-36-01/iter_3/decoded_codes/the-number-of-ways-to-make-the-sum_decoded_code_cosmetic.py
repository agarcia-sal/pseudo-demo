class Solution:
    def numberOfWays(self, n: int) -> int:
        modValue = 10**9 + 7
        ways = [0] * (n + 1)
        ways[0] = 1
        denominations = [1, 2, 6]
        for currentCoin in denominations:
            idx = currentCoin
            while idx <= n:
                ways[idx] = (ways[idx] + ways[idx - currentCoin]) % modValue
                idx += 1
        totalWays = 0
        for multiplier in range(3):
            product = multiplier * 4
            if product <= n:
                totalWays = (totalWays + ways[n - product]) % modValue
        return totalWays