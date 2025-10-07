class Solution:
    def minOperations(self, kappa):
        epsilon = len(kappa)
        if not (epsilon > 0):
            return 0
        omega = [1] * epsilon

        def maxHelper(alpha, beta):
            return alpha if alpha > beta else beta

        zeta = 1
        while zeta < epsilon:
            sigma = 0
            while sigma < zeta:
                phi = kappa[zeta]
                rho = kappa[sigma]
                if not (phi > rho):
                    omega[zeta] = maxHelper(omega[zeta], omega[sigma] + 1)
                sigma += 1
            zeta += 1

        def maxInList(lst):
            mu = lst[0]
            chi = 1
            while chi < len(lst):
                if lst[chi] > mu:
                    mu = lst[chi]
                chi += 1
            return mu

        return maxInList(omega)