from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        L = len(s)
        memo = {}

        def dfs(x: int) -> int:
            if x >= L:
                return 0
            if x in memo:
                return memo[x]

            C = defaultdict(int)
            F = defaultdict(int)
            o = L - x

            def recur(y: int, curAns: int) -> int:
                if y >= L:
                    return curAns
                cChar = s[y]

                oldCnt = C[cChar]
                if oldCnt > 0:
                    F[oldCnt] -= 1
                    if F[oldCnt] == 0:
                        del F[oldCnt]
                C[cChar] += 1
                newCnt = C[cChar]
                F[newCnt] = F.get(newCnt, 0) + 1

                oneKey = len(F) == 1
                updatedAns = curAns
                if oneKey:
                    t = 1 + dfs(y + 1)
                    if t < updatedAns:
                        updatedAns = t
                return recur(y + 1, updatedAns)

            o = recur(x, o)
            memo[x] = o
            return o

        return dfs(0)