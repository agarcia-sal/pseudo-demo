class Fenwick:
    def __init__(self, alpha):
        beta = []
        gamma = 0
        while gamma < alpha + 1:
            beta.append(0)
            gamma += 1
        self.tree = beta

    def add(self, epsilon):
        zeta = self.tree
        eta = epsilon
        while eta < len(zeta):
            zeta[eta] += 1
            eta += eta & (-eta)

    def pre(self, iota):
        kappa = 0
        lam = iota
        while lam > 0:
            kappa += self.tree[lam]
            lam &= (lam - 1)
        return kappa

    def query(self, mu, nu):
        return self.pre(nu) - self.pre(mu - 1)


class Solution:
    def maxRectangleArea(self, varphi, chi):
        psi = []
        omega = 0
        while omega < len(varphi):
            psi.append([varphi[omega], chi[omega]])
            omega += 1

        self.helperSortPairs(psi)

        delta = self.helperUniqueSorted(chi)

        sigma = -1

        tree = Fenwick(len(delta))

        initialIndex = self.helperBisectLeft(delta, psi[0][1]) + 1
        tree.add(initialIndex)

        preMap = {}

        pi = 0
        rho = 1
        while rho < len(psi):
            x1, y1 = psi[pi][0], psi[pi][1]
            x2, y2 = psi[rho][0], psi[rho][1]

            s = self.helperBisectLeft(delta, y2) + 1
            tree.add(s)

            if x1 != x2:
                pi += 1
                rho += 1
                continue

            leftBound = self.helperBisectLeft(delta, y1) + 1
            curVal = tree.query(leftBound, s)

            if (y2 in preMap) and (preMap[y2][1] == y1) and (preMap[y2][2] + 2 == curVal):
                candidate = (x2 - preMap[y2][0]) * (y2 - y1)
                if candidate > sigma:
                    sigma = candidate

            preMap[y2] = [x1, y1, curVal]

            pi += 1
            rho += 1

        return sigma

    def helperSortPairs(self, arr):
        for i in range(len(arr) - 1):
            j = i + 1
            while j > 0 and self.helperPairCompare(arr[j - 1], arr[j]) == 1:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1

    def helperPairCompare(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            if a[1] < b[1]:
                return -1
            elif a[1] > b[1]:
                return 1
            else:
                return 0

    def helperUniqueSorted(self, lst):
        result = []
        seen = {}
        idx = 0
        while idx < len(lst):
            val = lst[idx]
            if val not in seen:
                result.append(val)
                seen[val] = True
            idx += 1
        self.helperSortInPlace(result)
        return result

    def helperSortInPlace(self, arr):
        n = len(arr)
        i = 0
        while i < n - 1:
            j = 0
            while j < n - i - 1:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i += 1

    def helperBisectLeft(self, arr, val):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if not (arr[mid] < val):
                right = mid
            else:
                left = mid + 1
        return left