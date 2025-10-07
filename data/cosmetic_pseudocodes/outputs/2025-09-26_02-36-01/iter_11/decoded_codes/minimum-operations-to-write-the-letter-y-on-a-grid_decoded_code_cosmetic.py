from collections import defaultdict
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        alpha = len(grid)
        omega = alpha // 2
        sigmaSet = set()

        zeta = 0
        while zeta <= omega:
            sigmaSet.add((zeta, zeta))
            zeta += 1

        chi = 0
        while chi <= omega:
            sigmaSet.add((chi, alpha - chi - 1))
            chi += 1

        def insertRowTheta(kappa):
            if kappa > alpha - 1:
                return
            sigmaSet.add((kappa, omega))
            insertRowTheta(kappa + 1)

        insertRowTheta(omega)

        def countValues(cells, matrix):
            freqMap = defaultdict(int)
            for r, c in cells:
                val = matrix[r][c]
                freqMap[val] += 1
            return freqMap

        rho = countValues(sigmaSet, grid)

        complementPositions = []
        for p in range(alpha):
            for q in range(alpha):
                if (p, q) not in sigmaSet:
                    complementPositions.append((p, q))

        tau = countValues(complementPositions, grid)

        psi = inf

        for a in range(3):
            for b in range(3):
                if a != b:
                    sumRho = sum(rho.get(k, 0) for k in range(3))
                    sumTau = sum(tau.get(k, 0) for k in range(3))
                    op = (sumRho - rho.get(a, 0)) + (sumTau - tau.get(b, 0))
                    if op < psi:
                        psi = op

        return psi