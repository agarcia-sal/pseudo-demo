class Solution:
    def compressedString(self, word: str) -> str:
        outputList = []
        position = 0
        length = len(word)

        while position < length:
            currentChar = word[position]
            frequency = 0
            while position < length and word[position] == currentChar:
                frequency += 1
                position += 1
                if frequency == 9:  # 3 * 3 = 9
                    break
            outputList.append(str(frequency) + currentChar)

        combinedString = "".join(outputList)
        return combinedString