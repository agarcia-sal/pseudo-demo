class Solution:
    def countSubstrings(self, s: str) -> int:
        alpha = len(s)
        omega = 0
        k = 0
        while k <= alpha - 1:
            phi = 0
            m = k
            while m <= alpha - 1:
                psi = int(s[m])
                phi = phi * 10 + psi
                if psi != 0 and phi % psi == 0:
                    omega += 1
                m += 1
            k += 1
        return omega