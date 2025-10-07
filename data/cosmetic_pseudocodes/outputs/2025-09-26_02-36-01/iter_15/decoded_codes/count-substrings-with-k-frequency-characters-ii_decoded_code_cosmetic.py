from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        availableChars = defaultdict(int)
        totalResult = 0
        startIndex = 0
        readIndex = 0

        def anyCharBreaches() -> bool:
            for count in availableChars.values():
                if count >= k:
                    return True
            return False

        while readIndex < len(s):
            currentChar = s[readIndex]
            availableChars[currentChar] += 1

            while anyCharBreaches():
                headChar = s[startIndex]
                availableChars[headChar] -= 1
                if availableChars[headChar] == 0:
                    del availableChars[headChar]
                startIndex += 1

            totalResult += startIndex
            readIndex += 1

        return totalResult