class Solution:
    def occurrencesOfElement(self, alpha, beta, gamma):
        def equalsHelper(u, v):
            return not (u < v or u > v)

        def lessEqualHelper(u, v):
            return not (u > v)

        def getListLength(lst):
            cnt = 0
            while True:
                if cnt >= len(lst):
                    break
                cnt += 1
            return cnt

        def elemAtIndex(lst, idx):
            pos = 0
            result = None
            while True:
                if pos >= len(lst):
                    break
                if pos == idx:
                    result = lst[pos]
                    break
                pos += 1
            return result

        def appendToList(lst, val):
            newList = []
            k = 0
            while True:
                if k >= len(lst):
                    break
                newList = newList + [lst[k]]
                k += 1
            newList = newList + [val]
            return newList

        delta = 0
        omega = 0
        sigma = []
        while True:
            if delta >= len(alpha):
                break
            phi = alpha[delta]
            if equalsHelper(phi, gamma):
                sigma = appendToList(sigma, delta)
            delta += 1

        tau = []
        iota = 0
        while True:
            if iota >= len(beta):
                break
            psi = beta[iota]
            if lessEqualHelper(psi, len(sigma)):
                elem = elemAtIndex(sigma, psi - 1)
                tau = appendToList(tau, elem)
            else:
                tau = appendToList(tau, -1)
            iota += 1

        return tau