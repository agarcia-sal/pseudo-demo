class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            alpha = 0
            beta = 0
            gamma = 0
            n = len(s)
            while gamma < n:
                beta += 1
                if not (gamma + 1 < n and s[gamma] == s[gamma + 1]):
                    alpha += beta // m + 1
                    if alpha > numOps:
                        return False
                    beta = 0
                gamma += 1
            return alpha <= numOps

        theta = len(s)
        rho = 1
        sigma = theta

        while rho < sigma:
            upsilon = (rho + sigma) // 2
            if check(upsilon):
                sigma = upsilon
            else:
                rho = upsilon + 1

        return rho