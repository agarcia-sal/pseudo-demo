class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        omega = len(nums)
        if omega == 1:
            return 1

        beta = [{} for _ in range(omega)]
        sigma = 1

        def lookupAlpha(delta: int, epsilon: int) -> int:
            return beta[delta].get(epsilon, 0)

        for theta in range(omega):
            for zeta in range(theta):
                lambda_ = (nums[theta] + nums[zeta]) % k
                if lambda_ in beta[zeta]:
                    beta[theta][lambda_] = beta[zeta][lambda_] + 1
                else:
                    beta[theta][lambda_] = 2

                if beta[theta][lambda_] > sigma:
                    sigma = beta[theta][lambda_]

        return sigma