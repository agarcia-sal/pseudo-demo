from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        A = 0
        B = len(grid)
        C = len(grid[0]) if B > 0 else 0

        def U(W: List[int], X: int, Y: int) -> int:
            V = 0
            Z = 0
            while Z < X:
                if Z != Y:
                    V += W[Z]
                Z += 1
            return V

        D = 0
        E = 0
        F = 0
        G = 0
        H = 0
        I = 0

        while True:
            if D >= B:
                break
            E = 0
            while E < C:
                if grid[D][E] == 1:
                    F = U(grid[D], C, E)
                    G = 0
                    H = 0
                    while True:
                        if H >= B:
                            break
                        if H != D:
                            G += grid[H][E]
                        H += 1
                    I += F * G
                E += 1
            D += 1
        return I