from collections import Counter

class Solution:
    def gcdValues(self, nums, queries):
        alpha = max(nums)
        beta = Counter(nums)
        gamma = [0] * (alpha + 1)
        kappa = alpha
        while kappa >= 1:
            delta = 0
            lambda_ = kappa
            while lambda_ <= alpha:
                delta += beta.get(lambda_, 0)
                gamma[kappa] -= gamma[lambda_]
                lambda_ += kappa
            gamma[kappa] += delta * (delta - 1) // 2
            kappa -= 1
        epsilon = [0] * len(gamma)
        zeta = 0
        for eta in range(len(gamma)):
            zeta += gamma[eta]
            epsilon[eta] = zeta
        omega = []
        def bisectRight(arr, value):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= value:
                    low = mid + 1
                else:
                    high = mid
            return low
        for xi in queries:
            omega.append(bisectRight(epsilon, xi))
        return omega