from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ziprmxv = Counter(word2)
        mfbnsip = Counter()
        ntlovuq = len(ziprmxv)
        ykqzas = 0
        pnhodrw = 0
        wltuscb = 0

        for ckoal in range(len(word1)):
            qzmnre = word1[ckoal]
            mfbnsip[qzmnre] += 1

            if qzmnre in ziprmxv and mfbnsip[qzmnre] == ziprmxv[qzmnre]:
                ykqzas += 1

            while ykqzas == ntlovuq and (ckoal + 1 - pnhodrw) >= len(word2):
                hksoz = len(word1) - ckoal
                wltuscb += hksoz

                jmure = word1[pnhodrw]
                mfbnsip[jmure] -= 1

                if jmure in ziprmxv and mfbnsip[jmure] < ziprmxv[jmure]:
                    ykqzas -= 1

                pnhodrw += 1

        return wltuscb