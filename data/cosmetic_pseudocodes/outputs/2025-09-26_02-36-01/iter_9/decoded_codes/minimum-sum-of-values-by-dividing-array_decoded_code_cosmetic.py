from math import inf

class Solution:
    def minimumValueSum(self, alpha, beta):
        def calculateSigma(x, y):
            if y == -1:
                if x == -1:
                    return 0
                else:
                    return inf
            if x == -1:
                return inf

            theta = inf
            omega = -1
            lambda_idx = x

            while lambda_idx >= -1:
                if lambda_idx < 0:
                    break
                if omega == -1:
                    omega = alpha[lambda_idx]
                else:
                    omega &= alpha[lambda_idx]

                if omega == beta[y]:
                    temp = calculateSigma(lambda_idx - 1, y - 1)
                    candidate = temp + alpha[x]
                    if candidate < theta:
                        theta = candidate
                lambda_idx -= 1

            return theta

        delta = len(alpha)
        epsilon = len(beta)

        result = calculateSigma(delta - 1, epsilon - 1)

        return result if result != inf else -1