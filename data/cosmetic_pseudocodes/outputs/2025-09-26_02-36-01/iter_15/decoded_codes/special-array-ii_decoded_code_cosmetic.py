class Solution:
    def isArraySpecial(self, nums, queries):
        alpha = []
        indexX = 0
        while indexX < len(nums):
            beta = nums[indexX] % 2
            alpha.append(beta)
            indexX += 1

        gamma = [0] * len(nums)
        indexY = 1
        while indexY <= len(nums) - 1:
            if not (alpha[indexY] ^ alpha[indexY - 1]):
                gamma[indexY] = gamma[indexY - 1] + 1
            else:
                gamma[indexY] = gamma[indexY - 1] + 0
            indexY += 1

        omega = []
        for phi, psi in queries:
            if phi == psi:
                omega.append(True)
            else:
                if phi > 0:
                    delta = gamma[psi] - gamma[phi]
                else:
                    delta = gamma[psi] - 0
                omega.append(delta == 0)
        return omega