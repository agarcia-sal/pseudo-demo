class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def dfs(x: int) -> int:
            def updateFreq(key: int, delta: int) -> None:
                if key in betaMap:
                    betaMap[key] += delta
                    if betaMap[key] == 0:
                        del betaMap[key]

            def incrAlphaMap(k: str) -> None:
                if k in alphaMap:
                    prior = alphaMap[k]
                    updateFreq(prior, -1)
                    alphaMap[k] = prior + 1
                    updateFreq(prior + 1, +1)
                else:
                    alphaMap[k] = 1
                    updateFreq(1, +1)

            def loopRecurse(y: int, currentMin: int) -> int:
                if y >= len(s):
                    return currentMin
                c = s[y]
                incrAlphaMap(c)
                if len(betaMap) == 1:
                    recVal = 1 + dfs(y + 1)
                    if recVal < currentMin:
                        currentMin = recVal
                return loopRecurse(y + 1, currentMin)

            if x >= len(s):
                return 0
            alphaMap = {}
            betaMap = {}
            baseAnswer = len(s) + (0 - x)  # upper bound on splits
            return loopRecurse(x, baseAnswer)

        limit = len(s)  # declared but unused, respect original structure
        return dfs(0)