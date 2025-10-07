from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s, k):
        frequencyMap = defaultdict(int)
        totalSubstrings = 0
        leftIndex = 0
        currentIndex = 0

        while currentIndex < len(s):
            currentChar = s[currentIndex]
            frequencyMap[currentChar] += 1

            hasCharWithCountAtLeastK = False
            for key in frequencyMap.keys():
                if frequencyMap[key] >= k:
                    hasCharWithCountAtLeastK = True
                    break

            while hasCharWithCountAtLeastK:
                leftChar = s[leftIndex]
                frequencyMap[leftChar] -= 1
                if frequencyMap[leftChar] == 0:
                    del frequencyMap[leftChar]
                leftIndex += 1

                hasCharWithCountAtLeastK = False
                for key in frequencyMap.keys():
                    if frequencyMap[key] >= k:
                        hasCharWithCountAtLeastK = True
                        break

            totalSubstrings += leftIndex
            currentIndex += 1

        return totalSubstrings