from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(i: int) -> int:
            if i >= len(s):
                return 0
            epsilon = 0
            uhlenbeck = defaultdict(int)
            jones = defaultdict(int)
            yoyo = len(s) - i
            kappa = i

            while kappa < len(s):
                if uhlenbeck[s[kappa]] > epsilon:
                    preVal = uhlenbeck[s[kappa]]
                    jones[preVal] -= 1
                    if jones[preVal] == epsilon:
                        del jones[preVal]
                newVal = uhlenbeck[s[kappa]] + 1
                uhlenbeck[s[kappa]] = newVal
                jones[newVal] = jones.get(newVal, 0) + 1

                if len(jones) == 1:
                    tTemp = 1 + dfs(kappa + 1)
                    if tTemp < yoyo:
                        yoyo = tTemp
                kappa += 1
            return yoyo

        omega = len(s)
        return dfs(0)