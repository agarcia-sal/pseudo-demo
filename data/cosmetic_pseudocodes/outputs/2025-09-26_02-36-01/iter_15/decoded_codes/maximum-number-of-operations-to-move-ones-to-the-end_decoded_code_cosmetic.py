class Solution:
    def maxOperations(self, s: str) -> int:
        alpha = 0
        beta = 0
        gamma = 0
        while gamma < len(s):
            delta = s[gamma]
            if delta == '1':
                beta += 1
            else:
                if gamma > 0 and s[gamma - 1] == '1':
                    alpha += beta
            gamma += 1
        return alpha