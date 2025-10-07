class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        pAQdwTYG = {}
        GyheCvrK = {}
        AobrKhBm = 0

        oqWkJBvf = 0
        while oqWkJBvf < len(word):
            zOVszKKb = word[oqWkJBvf]
            if zOVszKKb not in pAQdwTYG:
                pAQdwTYG[zOVszKKb] = oqWkJBvf
            GyheCvrK[zOVszKKb] = oqWkJBvf
            oqWkJBvf += 1

        JmFVIlsS = "abcdefghijklmnopqrstuvwxyz"
        TzAwlMnD = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        hKaVjfqc = 0
        while hKaVjfqc < len(JmFVIlsS) and hKaVjfqc < len(TzAwlMnD):
            rMZksXZU = JmFVIlsS[hKaVjfqc]
            TMnxkbDa = TzAwlMnD[hKaVjfqc]

            if TMnxkbDa in GyheCvrK and rMZksXZU in pAQdwTYG:
                if GyheCvrK[TMnxkbDa] < pAQdwTYG[rMZksXZU]:
                    AobrKhBm += 1

            hKaVjfqc += 1

        return AobrKhBm