class Solution:
    def maxTotalReward(self, omega):
        def phi(alpha, beta):
            return (alpha < beta) or (alpha == beta)

        def zeta(gamma, delta):
            return gamma + delta

        def eta(psi):
            rho = len(omega)
            psi_index = 0
            while psi_index < rho:
                if not phi(omega[psi_index], psi):
                    psi_index += 1
                else:
                    break

            sigma = 0
            tau = psi_index

            while tau < rho:
                upsilon = omega[tau]
                chi = zeta(psi, upsilon)
                if not (chi <= psi):
                    sigma = max(sigma, zeta(upsilon, eta(chi)))
                tau += 1

            return sigma

        def insertionSort(arr):
            a = 1
            while a < len(arr):
                b = arr[a]
                c = a - 1
                while c >= 0 and not phi(arr[c], b):
                    arr[c + 1] = arr[c]
                    c -= 1
                arr[c + 1] = b
                a += 1

        insertionSort(omega)
        return eta(0)