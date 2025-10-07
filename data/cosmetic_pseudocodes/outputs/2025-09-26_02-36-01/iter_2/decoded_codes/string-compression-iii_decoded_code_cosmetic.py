class Solution:
    def compressedString(self, word: str) -> str:
        encoded = []
        position = 0
        length = len(word)
        while position < length:
            currentChar = word[position]
            tally = 0
            while position < length and word[position] == currentChar:
                tally += 1
                position += 1
                if tally == 9:
                    break
            encoded.append(str(tally) + currentChar)
        return ''.join(encoded)