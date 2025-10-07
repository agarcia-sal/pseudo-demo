class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        letters = [ch for ch in s]
        sortedLetters = []
        while letters:
            minChar = letters[0]
            minPos = 0
            for pos in range(1, len(letters)):
                if letters[pos] < minChar:
                    minChar = letters[pos]
                    minPos = pos
            sortedLetters.append(minChar)
            letters = letters[:minPos] + letters[minPos+1:]

        lengthVal = len(sortedLetters)
        half = lengthVal // 2

        midLeftChar = sortedLetters[half - 1]
        midChar = sortedLetters[half]

        if midChar == midLeftChar:
            idxI = half
            while idxI < lengthVal and sortedLetters[idxI] == sortedLetters[idxI - 1]:
                idxI += 1
            idxJ = half
            while idxJ < lengthVal and sortedLetters[idxJ] == sortedLetters[lengthVal - idxJ - 1]:
                if idxI >= lengthVal:
                    return "-1"
                sortedLetters[idxI], sortedLetters[idxJ] = sortedLetters[idxJ], sortedLetters[idxI]
                idxI += 1
                idxJ += 1

        pointer = 0
        while pointer < half:
            if sortedLetters[pointer] == sortedLetters[lengthVal - pointer - 1]:
                foundSwap = False
                searchIndex = half
                while searchIndex < lengthVal and not foundSwap:
                    if (sortedLetters[searchIndex] != sortedLetters[pointer] and
                        sortedLetters[searchIndex] != sortedLetters[lengthVal - pointer - 1]):
                        sortedLetters[searchIndex], sortedLetters[pointer] = sortedLetters[pointer], sortedLetters[searchIndex]
                        foundSwap = True
                    searchIndex += 1
                if not foundSwap:
                    return "-1"
            pointer += 1

        return "".join(sortedLetters)