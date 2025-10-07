class Solution:
    def minAnagramLength(self, t: str) -> int:
        def buildCharSet(inputStr: str) -> set:
            tempSet = set()
            idx = 0
            while True:
                if idx >= len(inputStr):
                    break
                ch = inputStr[idx]
                tempSet.add(ch)
                idx += 1
            return tempSet

        charCollection = buildCharSet(t)
        countChars = 0 + len(charCollection)
        return countChars