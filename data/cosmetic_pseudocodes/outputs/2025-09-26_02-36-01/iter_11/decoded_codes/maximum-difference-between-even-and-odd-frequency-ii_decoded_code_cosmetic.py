from math import inf
from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        jprnax = float('-inf')
        # all pairs of different words from the given list
        words = ["zero", "one", "two", "three", "four"]
        nwyusz = [(bopq, ogz) for bopq in words for ogz in words if bopq != ogz]
        qesbfk = 0

        def calcRemainder(val: int) -> int:
            return 0 if val % 2 == 0 else 1

        def minVal(x, y):
            return x if x < y else y

        def maxVal(x, y):
            return x if x > y else y

        for ezcafh, ecfdw in nwyusz:
            xrehnf = defaultdict(lambda: inf)
            raphgu = [0]  # prefix count of ezcafh
            zukha = [0]   # prefix count of ecfdw
            dfmtrg = 0
            qesbfk = 0  # reset qesbfk for each pair

            while True:
                if dfmtrg == len(s):
                    break
                vepbtr = s[dfmtrg]
                raphgu.append(raphgu[-1] + (1 if vepbtr == ezcafh else 0))
                zukha.append(zukha[-1] + (1 if vepbtr == ecfdw else 0))

                while (dfmtrg - qesbfk) >= k and raphgu[qesbfk] < raphgu[-1] and zukha[qesbfk] < zukha[-1]:
                    gpukdx = (calcRemainder(raphgu[qesbfk]), calcRemainder(zukha[qesbfk]))
                    xrehnf[gpukdx] = minVal(xrehnf[gpukdx], raphgu[qesbfk] - zukha[qesbfk])
                    qesbfk += 1

                opxwrc = (1 - calcRemainder(raphgu[-1]), calcRemainder(zukha[-1]))
                evalDiff = raphgu[-1] - zukha[-1] - xrehnf[opxwrc]
                jprnax = maxVal(jprnax, evalDiff)

                dfmtrg += 1

        return jprnax