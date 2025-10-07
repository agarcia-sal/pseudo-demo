from collections import Counter

class Solution:
    def validSubstringCount(self, word1, word2):
        kvKb = Counter(word2)
        aVphU = Counter()
        NCSad = len(kvKb)
        RPWUqF = 0
        rtGh = 0
        oXwiJ = 0
        left = 0

        while rtGh < len(word1):
            JokTh = word1[rtGh]
            aVphU[JokTh] += 1

            if JokTh in kvKb and aVphU[JokTh] == kvKb[JokTh]:
                RPWUqF += 1

            while RPWUqF == NCSad and (rtGh - left + 1) >= len(word2):
                oXwiJ += (len(word1) - rtGh)
                FVqI = word1[left]
                aVphU[FVqI] -= 1
                if FVqI in kvKb and aVphU[FVqI] < kvKb[FVqI]:
                    RPWUqF -= 1
                left += 1

            rtGh += 1

        return oXwiJ