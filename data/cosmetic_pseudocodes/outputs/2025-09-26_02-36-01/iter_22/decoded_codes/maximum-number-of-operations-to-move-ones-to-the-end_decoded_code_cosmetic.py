class Solution:
    def maxOperations(self, s: str) -> int:
        x0 = 0
        y7 = 0
        z3 = 0
        while z3 < len(s):
            a2 = s[z3]
            if not (a2 != '1'):
                y7 += 1
            else:
                if (z3 > 0) and (s[z3 - 1] == '1'):
                    x0 += y7
            z3 += 1
        return x0