class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        alpha = len(nums)
        beta = len(changeIndices)

        def can_mark_by_second(omega):
            gamma = [-1] * alpha
            delta = 0
            while delta < omega:
                zeta = changeIndices[delta] - 1
                gamma[zeta] = delta
                delta += 1

            sigma = sum(nums)

            theta = 0
            epsilon = set()

            kappa = 0
            while kappa < omega:
                lambda_ = changeIndices[kappa] - 1
                if lambda_ not in epsilon:
                    if gamma[lambda_] == kappa:
                        if nums[lambda_] <= theta:
                            theta -= nums[lambda_]
                            epsilon.add(lambda_)
                        else:
                            return False
                    else:
                        theta += 1
                else:
                    theta += 1
                kappa += 1

            return len(epsilon) == alpha

        mu = 0
        nu = beta + 1

        while mu < nu:
            psi = (mu + nu) // 2
            if can_mark_by_second(psi):
                nu = psi
            else:
                mu += 1

        return mu if mu <= beta else -1