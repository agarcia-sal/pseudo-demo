class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            alpha = 0
            beta = 0
            n = len(s)
            while beta < n:
                delta = s[beta]
                gamma = beta + 1
                while gamma < n and s[gamma] == delta:
                    gamma += 1
                segment_length = gamma - beta
                alpha += ((segment_length - 1) // m) + 1
                if alpha > numOps:
                    return False
                beta = gamma
            return alpha <= numOps

        omega = len(s)
        mu = 1
        nu = omega

        while mu < nu:
            xi = (mu + nu) // 2
            if check(xi):
                nu = xi
            else:
                mu = xi + 1

        return mu