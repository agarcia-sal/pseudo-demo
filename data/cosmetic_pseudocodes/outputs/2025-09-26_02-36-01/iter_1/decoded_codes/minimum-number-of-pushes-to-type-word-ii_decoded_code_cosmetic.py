class Solution:
    def minimumPushes(self, word: str) -> int:
        letterCounts = {}
        for char in word:
            letterCounts[char] = letterCounts.get(char, 0) + 1

        frequencyList = sorted(letterCounts.values(), reverse=True)

        totalPushes = 0
        pressesPerKey = 1
        keysUsed = 0

        i = 0
        while i < len(frequencyList):
            totalPushes += frequencyList[i] * pressesPerKey
            keysUsed += 1

            if keysUsed == 8:
                keysUsed = 0
                pressesPerKey += 1

            i += 1

        return totalPushes