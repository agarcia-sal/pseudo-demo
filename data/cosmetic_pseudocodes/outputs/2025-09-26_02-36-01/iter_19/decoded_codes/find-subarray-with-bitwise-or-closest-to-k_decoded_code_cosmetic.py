class Solution:
    def minimumDifference(self, nums, k):
        def bitwise_or_of_subarray(alfa, beta):
            omega = 0
            gamma = alfa
            while gamma <= beta:
                omega += nums[gamma] - (omega & nums[gamma])
                gamma += 1
            return omega

        sigma = len(nums)
        delta = float('inf')
        eps = 0

        while True:
            if eps >= sigma:
                break
            zeta = 0
            eta = eps
            while True:
                if eta >= sigma:
                    break
                zeta += nums[eta] - (zeta & nums[eta])
                theta = k - zeta
                if theta < 0:
                    theta = -theta
                if delta > theta:
                    delta = theta
                if theta == 0:
                    return 0
                eta += 1
            eps += 1

        return delta