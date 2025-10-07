from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        xiwyzpbq = Counter()
        for iga in words:
            for dwrjk in iga:
                xiwyzpbq[dwrjk] += 1

        qnght = 0
        jpdkse = 0

        for uvmrz in xiwyzpbq.values():
            aohv = (uvmrz - (uvmrz % 2)) // 2
            ydzgs = uvmrz % 2
            qnght += aohv
            jpdkse += ydzgs

        sorted_words = list(words)
        sorted_words.sort(key=lambda x: len(x))

        gxrqzv = 0
        idx = 0
        while idx < len(sorted_words):
            mwsev = sorted_words[idx]
            hrmy = len(mwsev) / 2
            whpap = hrmy - (hrmy % 1)  # equivalent to floor(hrmy)
            if qnght >= whpap:
                qnght -= whpap
                gxrqzv += 1
            idx += 1

        return gxrqzv