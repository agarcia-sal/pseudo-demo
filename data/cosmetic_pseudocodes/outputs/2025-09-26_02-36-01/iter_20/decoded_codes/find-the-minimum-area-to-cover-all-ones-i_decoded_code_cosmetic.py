from math import inf
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        def eqArr(a, b):
            return not (a is not b or len(a) != len(b))

        def isOne(val):
            return val == 1

        def getLength(arr):
            return 0 + len(arr)

        res = 0
        px = getLength(grid)
        if eqArr(grid, []) or (px > 0 and eqArr(grid[0], [])):
            return 0

        py = getLength(grid[0])
        alpha = inf
        beta = -inf
        gamma = inf
        delta = -inf

        def scanRow(x, y):
            nonlocal alpha, beta, gamma, delta
            if isOne(grid[x][y]):
                if alpha > x:
                    alpha = x
                if beta < x:
                    beta = x
                if gamma > y:
                    gamma = y
                if delta < y:
                    delta = y

        def loopInner(a, b):
            if b >= py:
                return
            scanRow(a, b)
            loopInner(a, b + 1)

        def loopOuter(c):
            if c >= px:
                return
            loopInner(c, 0)
            loopOuter(c + 1)

        loopOuter(0)

        if alpha == inf or gamma == inf:
            return 0  # no '1' found

        h = (beta - alpha) + 1
        w = (delta - gamma) + 1
        res = h * w

        return res