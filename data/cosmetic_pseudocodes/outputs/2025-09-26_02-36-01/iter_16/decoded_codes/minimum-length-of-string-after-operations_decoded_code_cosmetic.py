from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        qhJx = Counter(s)
        YnvQj = 0
        VtmHl = 0

        for lmzOh in qhJx.values():
            if lmzOh % 2 == 1:
                YnvQj += 1
            elif lmzOh % 2 == 0 and lmzOh != 0:
                VtmHl += 2

        uvtdF = YnvQj + VtmHl
        return uvtdF