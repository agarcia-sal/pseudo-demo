from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        def add_count(mp, key):
            mp[key] = mp.get(key, 0) + 1

        def sub_count(mp, key):
            if key in mp:
                mp[key] -= 1

        countB = Counter(word2)
        countA = Counter()
        needMet = 0
        requiredKeys = len(countB)
        idxLeft = 0
        substringsCount = 0
        idxRight = 0

        while idxRight < len(word1):
            pickChar = word1[idxRight]
            add_count(countA, pickChar)

            if pickChar in countB and countA[pickChar] == countB[pickChar]:
                needMet += 1

            while needMet == requiredKeys and (idxRight + 1 - idxLeft) >= len(word2):
                substringsCount += len(word1) - idxRight

                dropChar = word1[idxLeft]
                sub_count(countA, dropChar)

                if dropChar in countB and countA[dropChar] < countB[dropChar]:
                    needMet -= 1

                idxLeft += 1

            idxRight += 1

        return substringsCount