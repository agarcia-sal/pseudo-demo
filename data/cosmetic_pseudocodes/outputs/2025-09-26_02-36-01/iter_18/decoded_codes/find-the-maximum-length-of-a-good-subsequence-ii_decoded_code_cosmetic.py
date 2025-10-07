from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        alpha = len(nums)
        delta = [[0] * (k + 1) for _ in range(alpha)]
        omega = [defaultdict(int) for _ in range(k + 1)]
        sigma = [[0, 0, 0] for _ in range(k + 1)]
        rho = 0
        m = 0
        while m < alpha:
            z = nums[m]
            c = 0
            while c <= k:
                delta[m][c] = omega[c][z]
                if c != 0:
                    if sigma[c - 1][0] != z:
                        delta[m][c] = max(delta[m][c], sigma[c - 1][1])
                    else:
                        delta[m][c] = max(delta[m][c], sigma[c - 1][2])
                delta[m][c] += 1
                omega[c][z] = max(omega[c][z], delta[m][c])

                if sigma[c][0] != z:
                    if delta[m][c] >= sigma[c][1]:
                        sigma[c][2] = sigma[c][1]
                        sigma[c][1] = delta[m][c]
                        sigma[c][0] = z
                    else:
                        sigma[c][2] = max(sigma[c][2], delta[m][c])
                else:
                    sigma[c][1] = max(sigma[c][1], delta[m][c])

                rho = max(rho, delta[m][c])
                c += 1
            m += 1
        return rho