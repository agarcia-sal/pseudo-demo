class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            alpha = 0
            beta = 0
            n = len(s)
            while beta < n:
                gamma = 1
                while beta + 1 < n and s[beta] == s[beta + 1]:
                    gamma += 1
                    beta += 1
                delta = (gamma + m - 1) // m
                alpha += delta
                if alpha > numOps:
                    return False
                beta += 1
            return alpha <= numOps

        length_s = len(s)
        low_bound, up_bound = 1, length_s
        while low_bound < up_bound:
            middle = (low_bound + up_bound) // 2
            if check(middle):
                up_bound = middle
            else:
                low_bound = middle + 1
        return low_bound