from math import inf
from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        uH = len(grid)
        uW = len(grid[0])
        eT = self.gZ(uH, uW, inf)
        eT[0][0] = grid[0][0]
        Bc = -inf

        def Ol():
            for kM in range(1, uW):
                if eT[0][kM - 1] < grid[0][kM]:
                    eT[0][kM] = eT[0][kM - 1]
                else:
                    eT[0][kM] = grid[0][kM]

        def Gq():
            for an in range(1, uH):
                if eT[an - 1][0] < grid[an][0]:
                    eT[an][0] = eT[an - 1][0]
                else:
                    eT[an][0] = grid[an][0]

        def Yw():
            nonlocal Bc
            for td in range(1, uH):
                for bF in range(1, uW):
                    if eT[td - 1][bF] < eT[td][bF - 1]:
                        eT[td][bF] = eT[td - 1][bF]
                    else:
                        eT[td][bF] = eT[td][bF - 1]
                    sV = grid[td][bF] - eT[td][bF]
                    if sV > Bc:
                        Bc = sV

        Ol()
        Gq()
        Yw()

        return Bc

    def gZ(self, length1: int, length2: int, ValInit: float) -> List[List[float]]:
        Gv = []
        for _ in range(length1):
            YF = [ValInit] * length2
            Gv.append(YF)
        return Gv