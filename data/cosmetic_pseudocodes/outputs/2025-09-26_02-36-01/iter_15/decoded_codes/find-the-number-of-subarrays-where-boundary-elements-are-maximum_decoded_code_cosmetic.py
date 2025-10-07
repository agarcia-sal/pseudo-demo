from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        omega = defaultdict(list)
        kappa = 0
        while kappa < len(nums):
            phi = nums[kappa]
            omega[phi].append(kappa)
            kappa += 1

        psi = 0
        chi = list(omega.values())
        mu = len(chi)
        delta = 0
        while delta < mu:
            epsilon = chi[delta]
            nu = len(epsilon)
            alpha = 0
            while alpha < nu:
                beta = alpha
                while beta < nu:
                    gamma = epsilon[alpha]
                    eta = epsilon[beta]
                    zeta = gamma
                    iota = eta
                    sublist = []
                    lax = zeta
                    while lax <= iota:
                        sublist.append(nums[lax])
                        lax += 1

                    maxVal = sublist[0]
                    index_max = 1
                    while index_max < len(sublist):
                        if sublist[index_max] > maxVal:
                            maxVal = sublist[index_max]
                        index_max += 1

                    if maxVal == nums[gamma]:
                        psi += 1

                    beta += 1
                alpha += 1
            delta += 1

        return psi