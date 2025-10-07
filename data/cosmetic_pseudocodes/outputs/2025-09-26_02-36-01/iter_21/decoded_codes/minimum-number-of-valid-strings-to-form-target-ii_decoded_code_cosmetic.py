class Solution:
    def minValidStrings(self, words, target):
        A = set()
        for B in words:
            for y in range(1, len(B) + 1):
                A.add(B[:y])

        M = len(target)
        Q = [float('inf')] * (M + 1)
        Q[0] = 0

        for p in range(1, M + 1):
            for r in range(1, p + 1):
                # substring of target starting at r for length (p - r + 1)
                substr = target[r - 1:p]
                if substr in A:
                    s = Q[r - 1] + 1
                    if Q[p] > s:
                        Q[p] = s
        res = Q[M]
        return -1 if res == float('inf') else res