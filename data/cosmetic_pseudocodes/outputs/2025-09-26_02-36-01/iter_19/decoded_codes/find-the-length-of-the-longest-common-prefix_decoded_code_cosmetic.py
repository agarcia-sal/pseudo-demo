class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        omega = set()
        for delta in arr1:
            phi = str(delta)
            kappa = 1
            while kappa <= len(phi):
                psi = phi[:kappa]
                omega.add(psi)
                kappa += 1

        sigma = set()
        theta = 0
        for beta in arr2:
            gamma = str(beta)
            for lambd in range(1, len(gamma) + 1):
                mu = gamma[:lambd]
                sigma.add(mu)

        for alpha in omega:
            if alpha in sigma:
                if len(alpha) > theta:
                    theta = len(alpha)

        return theta