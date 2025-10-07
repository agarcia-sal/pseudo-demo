class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        initialPositions = {}
        finalPositions = {}
        idx = 0
        while idx < len(word):
            charAtIdx = word[idx]
            if charAtIdx not in initialPositions:
                initialPositions[charAtIdx] = idx
            finalPositions[charAtIdx] = idx
            idx += 1

        specialCount = 0
        lowercaseLetters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        uppercaseLetters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        pos = 0
        while pos < len(lowercaseLetters):
            lowerChar = lowercaseLetters[pos]
            upperChar = uppercaseLetters[pos]
            if (lowerChar in finalPositions) and (upperChar in initialPositions):
                lowerFinalPos = finalPositions[lowerChar]
                upperInitialPos = initialPositions[upperChar]
                if lowerFinalPos < upperInitialPos:
                    specialCount += 1
            pos += 1

        return specialCount