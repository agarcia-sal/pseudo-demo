class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(beta):
            omega = -1
            phi = 0
            for xi in nums:
                if omega == -1:
                    omega = xi
                else:
                    omega &= xi
                if (omega & beta) == 0:
                    omega = -1
                else:
                    phi += 1
                    if phi > k:
                        return False
            return True

        delta = (1 << 30) - 1
        sigma = delta
        for tau in range(30):
            epsilon = 1 << tau
            if (sigma & epsilon) == 0:
                continue
            if canAchieve((~sigma) ^ epsilon):
                sigma &= ~epsilon
        return sigma