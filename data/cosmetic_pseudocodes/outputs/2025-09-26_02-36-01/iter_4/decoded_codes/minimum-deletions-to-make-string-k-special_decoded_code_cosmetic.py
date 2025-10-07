from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        charCount = Counter(word)
        freqList = sorted(charCount.values())

        minDel = float('inf')
        for i in range(len(freqList)):
            maxFreqAllowed = freqList[i] + k
            deleteCount = 0
            for j in range(i + 1, len(freqList)):
                if freqList[j] > maxFreqAllowed:
                    deleteCount += freqList[j] - maxFreqAllowed
            for m in range(i):
                deleteCount += freqList[m]
            if deleteCount < minDel:
                minDel = deleteCount

        return minDel