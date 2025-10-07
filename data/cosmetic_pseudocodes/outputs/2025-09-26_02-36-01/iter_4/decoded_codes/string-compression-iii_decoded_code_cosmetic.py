class Solution:
    def compressedString(self, word: str) -> str:
        compressedList = []
        index = 0
        n = len(word)
        while index < n:
            currentChar = word[index]
            tally = 0
            while index < n and word[index] == currentChar and tally < 9:
                tally += 1
                index += 1
            compressedList.append(str(tally) + currentChar)
        return ''.join(compressedList)