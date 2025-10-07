class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        mapA = {}
        mapB = {}
        for idx1, ch1 in enumerate(word):
            if ch1 not in mapA:
                mapA[ch1] = idx1
            mapB[ch1] = idx1
        ctr = 0
        for iter1 in range(len("abcdefghijklmnopqrstuvwxyz")):
            for iter2 in range(len("ABCDEFGHIJKLMNOPQRSTUVWXYZ")):
                ch1 = "abcdefghijklmnopqrstuvwxyz"[iter1]
                ch2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[iter2]
                cond1 = ch1 in mapB
                cond2 = ch2 in mapA
                if cond1 and cond2:
                    valA = mapB[ch1]
                    valB = mapA[ch2]
                    if valA < valB:
                        ctr += 1
        return ctr