from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        alpha = len(s)
        delta_zeros = [0] * (alpha + 1)
        epsilon_ones = [0] * (alpha + 1)

        gamma = 0
        while gamma < alpha:
            delta_zeros[gamma + 1] = delta_zeros[gamma] + (1 if s[gamma] == '0' else 0)
            epsilon_ones[gamma + 1] = epsilon_ones[gamma] + (1 if s[gamma] == '1' else 0)
            gamma += 1

        def count_valid_substrings(x: int, y: int) -> int:
            omega = 0
            theta = x
            while theta <= y:
                mu = theta
                nu = y + 1
                while mu < nu:
                    pi = (mu + nu) // 2
                    sigma = delta_zeros[pi + 1] - delta_zeros[theta]
                    tau = epsilon_ones[pi + 1] - epsilon_ones[theta]
                    if sigma <= k or tau <= k:
                        mu = pi + 1
                    else:
                        nu = pi
                rho = mu - 1
                if rho >= theta:
                    omega += (rho - theta + 1)
                theta += 1
            return omega

        result = []
        xi = 0
        while xi < len(queries):
            lamda = queries[xi][0]
            kappa = queries[xi][1]
            result.append(count_valid_substrings(lamda, kappa))
            xi += 1

        return result