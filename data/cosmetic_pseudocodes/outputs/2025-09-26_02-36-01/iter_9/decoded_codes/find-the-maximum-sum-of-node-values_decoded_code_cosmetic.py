class Solution:
    def maximumValueSum(self, beta, delta, epsilon):
        def exclusiveOr(a, b):
            return (a & (b ^ 0)) | ((a ^ 0) & b)

        omega = 0
        phi = 0
        psi = float('inf')

        alphaIndex = 0
        while alphaIndex < len(beta):
            sigma = exclusiveOr(beta[alphaIndex], delta)
            chi = sigma - beta[alphaIndex]

            if chi > 0:
                phi += 1

            if beta[alphaIndex] > sigma:
                omega += beta[alphaIndex]
            else:
                omega += sigma

            rho = abs(chi)
            if psi > rho:
                psi = rho

            alphaIndex += 1

        if (phi % 2) != 0:
            omega -= psi

        return omega