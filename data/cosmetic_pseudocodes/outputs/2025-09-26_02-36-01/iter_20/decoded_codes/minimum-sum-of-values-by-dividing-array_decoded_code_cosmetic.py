from math import inf

class Solution:
    def minimumValueSum(self, nums, andValues):
        lengthX = len(nums)
        lengthY = len(andValues)

        def computeAlpha(beta, gamma):
            if gamma == -1:
                if beta == -1:
                    return 0
                else:
                    return inf
            if beta == -1:
                return inf

            zeta = inf
            omega = -1
            indexDelta = beta

            while True:
                if omega == -1:
                    omega = nums[indexDelta]
                else:
                    omega &= nums[indexDelta]

                if omega == andValues[gamma]:
                    psi = computeAlpha(indexDelta - 1, gamma - 1)
                    if psi + nums[beta] < zeta:
                        zeta = psi + nums[beta]

                if indexDelta <= -1:
                    break
                indexDelta -= 1

            return zeta

        sigma = computeAlpha(lengthX - 1, lengthY - 1)
        return sigma if sigma != inf else -1