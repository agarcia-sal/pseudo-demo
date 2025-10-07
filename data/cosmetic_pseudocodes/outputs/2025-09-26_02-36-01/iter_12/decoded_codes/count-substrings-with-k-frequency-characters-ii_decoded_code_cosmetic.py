class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def hasCharAtLeastK(freqMap):
            # Check if any character count in freqMap is >= k
            for count in freqMap.values():
                if count >= k:
                    return True
            return False

        def incrementCharCount(char, map_):
            map_[char] = map_.get(char, 0) + 1

        def decrementCharCount(char, map_):
            map_[char] -= 1
            if map_[char] == 0:
                del map_[char]

        def addToTotal(currentTotal, value):
            return currentTotal + value

        frequencyMap = dict()
        totalSubstrings = 0
        windowStart = 0

        position = 0
        while position < len(s):
            currentChar = s[position]
            incrementCharCount(currentChar, frequencyMap)

            while hasCharAtLeastK(frequencyMap):
                charToRemove = s[windowStart]
                decrementCharCount(charToRemove, frequencyMap)
                windowStart += 1

            totalSubstrings = addToTotal(totalSubstrings, windowStart)
            position += 1

        return totalSubstrings