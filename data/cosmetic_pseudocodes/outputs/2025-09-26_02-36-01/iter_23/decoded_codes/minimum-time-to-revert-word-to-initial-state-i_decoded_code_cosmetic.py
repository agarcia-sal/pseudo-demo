class Solution:
    def minimumTimeToInitialState(self, k: int) -> int:
        word = k
        pqr = len(word)
        xyz = 1

        def checkCondition(a: int, b: int, c: int, d: str) -> bool:
            return (a * b >= c) or (d[a * b:] == d[:c - a * b])

        def loopRecursion(u: int) -> int:
            if checkCondition(u, k, pqr, word):
                return u
            else:
                return loopRecursion(u + 1)

        return loopRecursion(xyz)