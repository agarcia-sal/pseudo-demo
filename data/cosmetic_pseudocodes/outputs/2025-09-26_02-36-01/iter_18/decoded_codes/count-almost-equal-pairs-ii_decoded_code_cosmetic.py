from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        eta = 0
        phi = defaultdict(int)

        epsilon = 0
        while epsilon < len(nums):
            alpha = nums[epsilon]
            rho = set()
            rho.add(alpha)
            omega = list(str(alpha))
            kappa = len(omega)

            delta = 0
            while delta <= kappa - 1:
                gamma = 0
                while gamma <= delta - 1:
                    # swap omega[gamma] with omega[delta]
                    omega[gamma], omega[delta] = omega[delta], omega[gamma]

                    sigma = int("".join(omega))
                    rho.add(sigma)

                    psi = gamma + 1
                    while psi <= kappa - 1:
                        mu = gamma + 1
                        while mu <= psi - 1:
                            # swap omega[mu] with omega[psi]
                            omega[mu], omega[psi] = omega[psi], omega[mu]

                            upsilon = int("".join(omega))
                            rho.add(upsilon)

                            # swap back omega[mu] with omega[psi]
                            omega[psi], omega[mu] = omega[mu], omega[psi]

                            mu += 1
                        psi += 1

                    # swap back omega[gamma] with omega[delta]
                    omega[delta], omega[gamma] = omega[gamma], omega[delta]

                    gamma += 1
                delta += 1

            theta = 0
            for sigma in rho:
                theta += phi[sigma]

            eta += theta
            phi[alpha] += 1
            epsilon += 1

        return eta