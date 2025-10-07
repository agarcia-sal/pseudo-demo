from typing import List


def anti_shuffle(inputString: str) -> str:
    def processWordsRecursively(wordSequence: List[str], accumulator: List[str]) -> str:
        if not wordSequence:
            return " ".join(accumulator)

        singleWord = wordSequence[0]
        remainingWords = wordSequence[1:]

        charactersArray: List[str] = [char for char in singleWord]
        sortedChars = sorted(charactersArray)

        reconstructedWord = ""
        while sortedChars:
            nextChar = sortedChars[0]
            sortedChars = sortedChars[1:]
            reconstructedWord += nextChar

        return processWordsRecursively(remainingWords, accumulator + [reconstructedWord])

    words: List[str] = []
    currentIndex = 0
    wordStart = 0
    length = len(inputString)

    while currentIndex < length:
        if inputString[currentIndex] == " ":
            currentWord = ""
            for i in range(wordStart, currentIndex):
                currentWord += inputString[i]
            words.append(currentWord)
            wordStart = currentIndex + 1
        currentIndex += 1

    if wordStart < length:
        lastWord = ""
        for j in range(wordStart, length):
            lastWord += inputString[j]
        words.append(lastWord)

    return processWordsRecursively(words, [])