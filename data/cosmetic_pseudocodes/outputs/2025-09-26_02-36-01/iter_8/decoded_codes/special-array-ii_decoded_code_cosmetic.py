from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        epsilon = 0
        omega = []

        delta = len(nums)
        iota = 0
        while iota < delta:
            # modulo divisor is 1 + epsilon + 1 = 2
            kappa = nums[iota] % 2
            omega.append(kappa)
            iota += 1

        alpha = [0] * delta

        theta = 1
        while theta < delta:
            if omega[theta] == omega[theta - 1]:
                alpha[theta] = alpha[theta - 1] + 1
            else:
                alpha[theta] = alpha[theta - 1]
            theta += 1

        beta = []
        for mu, nu in queries:
            if mu == nu:
                beta.append(True)
            else:
                sigma = alpha[mu - 1] if mu > 0 else 0
                rho = alpha[nu] - sigma
                beta.append(rho == 0)

        return beta