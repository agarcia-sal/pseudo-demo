class Solution:
    def minOperations(self, nums):
        alpha = len(nums)
        if not (alpha > 0):
            return 0

        omega = [1] * alpha

        beta = 1
        while beta < alpha:
            gamma = 0
            while gamma < beta:
                if nums[beta] <= nums[gamma]:
                    theta = omega[gamma] + 1
                    if omega[beta] < theta:
                        omega[beta] = theta
                gamma += 1
            beta += 1

        delta = omega[0]
        iota = 1
        while iota < alpha:
            if omega[iota] > delta:
                delta = omega[iota]
            iota += 1

        return delta