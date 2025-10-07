from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freqWord2 = Counter(word2)
        freqWindow = Counter()
        neededChars = len(freqWord2)
        matchedChars = 0
        startIndex = 0
        substringCount = 1  # (1 + 1) - 1 = 1

        pointer = 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while pointer < len_word1:
            currentChar = word1[pointer]
            freqWindow[currentChar] += 1

            # Increase matchedChars when a char count matches freqWord2 exactly
            if freqWord2[currentChar] != 0 and freqWindow[currentChar] == freqWord2[currentChar]:
                matchedChars += 1

            # Try to shrink from the left if all chars matched and window length >= len_word2
            while matchedChars == neededChars and (pointer + 1) >= len_word2:
                substringCount += len_word1 - pointer

                startChar = word1[startIndex]
                freqWindow[startChar] -= 1
                if freqWord2[startChar] != 0 and freqWindow[startChar] < freqWord2[startChar]:
                    matchedChars -= 1
                startIndex += 1

            pointer += 1

        return substringCount