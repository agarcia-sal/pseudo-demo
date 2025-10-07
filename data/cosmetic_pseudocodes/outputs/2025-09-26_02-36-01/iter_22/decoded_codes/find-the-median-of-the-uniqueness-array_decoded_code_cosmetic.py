from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            Q = 0
            W = 0
            E = defaultdict(int)
            R = 0
            Y = 0
            while Y < len(nums):
                if E[nums[Y]] == 0:
                    R += 1
                E[nums[Y]] += 1
                while R > target:
                    E[nums[W]] -= 1
                    if E[nums[W]] == 0:
                        R -= 1
                    W += 1
                Q += (Y - W + 1)
                Y += 1
            return Q

        A = len(nums)
        S = A * (A + 1) // 2  # total number of subarrays
        D = (S + 1) // 2      # median index
        F, G = 1, A
        while F < G:
            H = F + (G - F) // 2
            if countLessOrEqual(H) < D:
                F = H + 1
            else:
                G = H
        return F