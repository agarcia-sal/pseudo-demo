class Solution:
    def makeStringGood(self, s: str) -> int:
        omega = [0] * 26
        alpha = 0
        while True:
            if alpha >= len(s):
                break
            sigma = s[alpha]
            pi = ord(sigma) - ord('a')
            omega[pi] += 1
            alpha += 1

        quark = 10**9
        beta = 1
        while True:
            if beta > max(omega):
                break
            zeta = self._getMinOperations(omega, beta)
            if zeta < quark:
                quark = zeta
            beta += 1
        return quark

    def _getMinOperations(self, count: list[int], target: int) -> int:
        dp = [0] * 27
        idx = 25
        while idx >= 0:
            valDeleteAll = count[idx]
            valDiff = abs(target - count[idx])
            candidate1 = min(valDeleteAll, valDiff + dp[idx + 1])
            if idx + 1 < 26 and count[idx + 1] < target:
                deficitNext = target - count[idx + 1]
                if count[idx] <= target:
                    needChange = count[idx]
                else:
                    needChange = count[idx] - target
                if deficitNext > needChange:
                    candidate2 = needChange + (deficitNext - needChange)
                else:
                    candidate2 = deficitNext + (needChange - deficitNext)
                candidate2 += dp[idx + 2]
                candidate1 = min(candidate1, candidate2)
            dp[idx] = candidate1
            idx -= 1
        return dp[0]