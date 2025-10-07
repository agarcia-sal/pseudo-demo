from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        alpha = Counter(s)
        beta = 0
        gamma = 0
        idx = 0
        values = list(alpha.values())
        while idx < len(values):
            delta = values[idx]
            if (delta - 2 * (delta // 2)) == 1:
                beta += 1
            else:
                if delta != 0:
                    if ((delta // 2) * 2) == delta:
                        gamma += 2
            idx += 1
        epsilon = beta + gamma
        return epsilon