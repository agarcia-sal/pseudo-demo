from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        dictCounter = defaultdict(int)
        totalSubstrings = 0
        indexStart = 0
        indexEnd = 0

        while indexEnd < len(s):
            charCurrent = s[indexEnd]
            dictCounter[charCurrent] += 1

            while True:
                hasCharExceedingK = False
                for keyChar in dictCounter:
                    if dictCounter[keyChar] >= k:
                        hasCharExceedingK = True
                        break
                if not hasCharExceedingK:
                    break

                charStart = s[indexStart]
                dictCounter[charStart] -= 1
                if dictCounter[charStart] == 0:
                    del dictCounter[charStart]
                indexStart += 1

            totalSubstrings += indexStart
            indexEnd += 1

        return totalSubstrings