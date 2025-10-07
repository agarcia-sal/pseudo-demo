class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        length = len(word)
        while i < length:
            currentChar = word[i]
            frequency = 0
            while i < length and word[i] == currentChar and frequency < 9:
                frequency += 1
                i += 1
            comp.append(str(frequency) + currentChar)
        return "".join(comp)