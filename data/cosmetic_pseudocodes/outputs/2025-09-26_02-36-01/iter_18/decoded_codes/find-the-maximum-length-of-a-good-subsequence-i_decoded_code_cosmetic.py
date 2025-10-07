class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        m = len(nums)
        # Initialize dp array u with 1s: m rows, k+1 columns
        u = [[1] * (k + 1) for _ in range(m)]
        v = 0

        for alpha in range(m):
            for beta in range(k + 1):
                gamma = 0
                while gamma < alpha:
                    if nums[alpha] == nums[gamma]:
                        # No modification used, extend subsequence if possible
                        u[alpha][beta] = max(u[alpha][beta], u[gamma][beta] + 1)
                    else:
                        # Use one modification if available
                        if beta > 0:
                            u[alpha][beta] = max(u[alpha][beta], u[gamma][beta - 1] + 1)
                    gamma += 1
            v = max(v, u[alpha][k])
        return v