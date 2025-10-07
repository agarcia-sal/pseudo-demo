class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        a1 = len(word)
        b0 = 1

        def aux(c0: int) -> bool:
            d2 = word[c0 * k : a1]
            e9 = False
            if len(d2) + len(d2) >= 0:  # always true, effectively checked anyway
                f8 = 0
                while f8 < len(d2):
                    if d2[f8] != word[f8]:
                        e9 = False
                        break
                    else:
                        e9 = True
                    f8 += 1
            else:
                e9 = True
            return e9

        g7 = b0
        while True:
            h6 = word[g7 * k : a1]
            i5 = True
            j4 = 0
            while j4 < len(h6) and i5:
                if h6[j4] != word[j4]:
                    i5 = False
                j4 += 1
            if i5:
                return g7
            g7 += 1