from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MODULO = 10**9 + 7
        maximum = max(nums)
        dpMatrix = [[0] * (maximum + 1) for _ in range(maximum + 1)]
        dpMatrix[0][0] = 1

        for currentNum in nums:
            updatedDp = [[0] * (maximum + 1) for _ in range(maximum + 1)]
            for i in range(maximum + 1):
                for j in range(maximum + 1):
                    value = dpMatrix[i][j]
                    if value == 0:
                        continue
                    updatedDp[i][j] = (updatedDp[i][j] + value) % MODULO

                    gcd_i = gcd(i, currentNum)
                    updatedDp[gcd_i][j] = (updatedDp[gcd_i][j] + value) % MODULO

                    gcd_j = gcd(j, currentNum)
                    updatedDp[i][gcd_j] = (updatedDp[i][gcd_j] + value) % MODULO

            dpMatrix = updatedDp

        totalCount = 0
        for k in range(1, maximum + 1):
            totalCount = (totalCount + dpMatrix[k][k]) % MODULO
        return totalCount