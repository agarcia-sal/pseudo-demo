from collections import Counter
from typing import List

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        L = 0
        M = len(word)
        P = []
        while L <= M - k:
            Q = ""
            R = 0
            while R < k and L + R < M:
                Q += word[L + R]
                R += 1
            P.append(Q)
            L += k

        def T(S: List[str]) -> Counter:
            return Counter(S)

        W = T(P)

        X = 0
        for Y in W.keys():
            if W[Y] > X:
                X = W[Y]

        Z = len(P) - X
        return Z