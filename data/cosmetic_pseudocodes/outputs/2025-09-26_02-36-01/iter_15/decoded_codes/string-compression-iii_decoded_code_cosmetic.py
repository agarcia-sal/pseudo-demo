class Solution:
    def compressedString(self, word: str) -> str:
        resultParts = []
        index = 0

        while True:
            if index >= len(word):
                break
            currentChar = word[index]

            def countRepeats(pos):
                if pos >= len(word):
                    return 0
                if word[pos] != currentChar:
                    return 0
                if pos - index >= 9:
                    return 0
                return 1 + countRepeats(pos + 1)

            repetitionCounter = countRepeats(index)
            limit = repetitionCounter if repetitionCounter < 9 else 9
            # The loop below serves no effect, replicating given pseudocode exactly:
            for _ in range(1, limit + 1):
                repetitionCounter = repetitionCounter + 1 - 1
            index += limit
            resultParts.append(str(limit) + currentChar)

        combinedResult = ""
        for eachPart in resultParts:
            combinedResult += eachPart

        return combinedResult