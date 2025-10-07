from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def uniqueElements(inputList: List[int]) -> Set[int]:
            tau = set()
            i = 0
            while i < len(inputList):
                e = inputList[i]
                if e not in tau:
                    tau.add(e)
                i += 1
            return tau

        def intersectionSets(a: Set[int], b: Set[int]) -> Set[int]:
            u = set()
            iterList = list(a)
            j = 0
            while j < len(iterList):
                val = iterList[j]
                if val in b:
                    u.add(val)
                j += 1
            return u

        def differenceSets(orig: Set[int], sub: Set[int]) -> Set[int]:
            w = set()
            for item in orig:
                if item not in sub:
                    w.add(item)
            return w

        def minVal(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def maxVal(a: int, b: int) -> int:
            if a > b:
                return a
            else:
                return b

        beta = 0
        omega = 0
        delta = len(nums1)
        gamma = delta // 2
        alpha = set()
        zeta = set()
        kappa = set()
        lambda_ = set()  # 'lambda' is a reserved keyword in Python
        mu = 0
        nu = 0
        xi = 0
        rho = 0
        sigma = 0

        alpha = uniqueElements(nums1)
        zeta = uniqueElements(nums2)

        kappa = intersectionSets(alpha, zeta)

        lambda_ = differenceSets(alpha, kappa)
        beta = differenceSets(zeta, kappa)

        mu = minVal(gamma, len(lambda_))
        nu = minVal(gamma, len(beta))
        xi = maxVal(0, gamma - mu)
        rho = maxVal(0, gamma - nu)

        sigma = mu + nu + minVal(xi + rho, len(kappa))

        return sigma