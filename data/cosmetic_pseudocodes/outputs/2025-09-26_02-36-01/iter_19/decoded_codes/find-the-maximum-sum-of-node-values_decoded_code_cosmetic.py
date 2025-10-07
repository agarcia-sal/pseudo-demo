from math import inf

class Solution:
    def maximumValueSum(self, nums, k, edges):
        self.alpha = 0
        self.delta = 0
        self.omega = inf
        self.phi = 1

        def processLoop(beta):
            if beta == len(nums):
                return
            rho = nums[beta] ^ k
            sigma = rho - nums[beta]
            if sigma > 0:
                self.delta += self.phi
            self.alpha += max(nums[beta], rho)
            self.omega = min(self.omega, abs(sigma))
            processLoop(beta + 1)

        processLoop(0)
        if (self.delta % 2) != 0:
            self.alpha -= self.omega
        return self.alpha