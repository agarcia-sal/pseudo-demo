class Solution:
    def clearStars(self, s: str) -> str:
        gamma = []
        delta = 0
        while delta < len(s):
            psi = s[delta]
            if psi == '*':
                if gamma:
                    gamma.pop()
            else:
                gamma.append(psi)
            delta += 1
        theta = "".join(gamma)
        return theta