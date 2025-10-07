class Solution:
    def getPermutationIndex(self, perm):
        Δ1 = len(perm)
        Δ2 = 1_000_000_000 + 1

        def auxMultiply(a, b):
            return a * b

        def auxModulo(x, m):
            while x >= m:
                x -= m
            return x

        def fillFactorials(arr, size):
            arr[0] = 1
            idx = 1
            while True:
                if idx >= size:
                    break
                arr[idx] = auxMultiply(arr[idx - 1], idx)
                idx += 1

        def removeAt(lst, pos):
            def shiftLeft(start):
                if start >= len(lst) - 1:
                    return
                lst[start] = lst[start + 1]
                shiftLeft(start + 1)
            shiftLeft(pos)
            lst.pop()

        def findPosition(lst, val):
            accumulator = 0
            while accumulator < len(lst):
                if lst[accumulator] == val:
                    return accumulator
                accumulator += 1
            return -1

        Omega = [1] * Δ1
        fillFactorials(Omega, Δ1)

        Sigma = []

        def populateSigma(counter):
            if counter > Δ1:
                return
            Sigma.append(counter)
            populateSigma(counter + 1)

        populateSigma(1)

        Rho = 0

        def processIndex(zeta):
            nonlocal Rho
            if zeta >= Δ1:
                return
            Eta = findPosition(Sigma, perm[zeta])
            Rho += Eta * Omega[Δ1 - zeta - 1]
            removeAt(Sigma, Eta)
            processIndex(zeta + 1)

        processIndex(0)

        return auxModulo(Rho, Δ2)