from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        memo = {}

        def rho(alpha: int) -> int:
            if alpha >= n:
                return 0

            if alpha in memo:
                return memo[alpha]

            phi = defaultdict(int)
            psi = defaultdict(int)
            omega = n - alpha
            beta = alpha

            while beta < n:
                gamma = s[beta]

                # Decrement count for previous frequency of gamma
                prev_count = phi[gamma]
                if prev_count != 0:
                    psi[prev_count] -= 1
                    if psi[prev_count] == 0:
                        del psi[prev_count]

                # Increment count for gamma
                phi[gamma] += 1
                curr_count = phi[gamma]
                psi[curr_count] = psi.get(curr_count, 0) + 1

                if len(psi) == 1:
                    delta = 1 + rho(beta + 1)
                    if delta < omega:
                        omega = delta
                beta += 1

            memo[alpha] = omega
            return omega

        return rho(0)