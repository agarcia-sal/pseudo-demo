class Solution:
    def compressedString(self, word: str) -> str:
        resultPieces = []
        position = 0
        while position < len(word):
            currentChar = word[position]
            tally = 0
            while position < len(word) and word[position] == currentChar:
                tally += 1
                position += 1
                if tally >= 9:
                    break
            segment = str(tally) + currentChar
            resultPieces.append(segment)
        output = ""
        idx = 0
        while idx < len(resultPieces):
            output += resultPieces[idx]
            idx += 1
        return output