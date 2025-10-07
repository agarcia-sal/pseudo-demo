from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    def countOccurrences(target: str, sequence: list[str], index: int, total: int) -> int:
        if index >= len(sequence):
            return total
        if sequence[index] == target:
            return countOccurrences(target, sequence, index + 1, total + 1)
        return countOccurrences(target, sequence, index + 1, total)

    lettersList = test_string.split(" ")
    freqDict: Dict[str, int] = {}
    maxFreq = 0

    def findMaxFrequency(idx: int) -> None:
        nonlocal maxFreq
        if idx >= len(lettersList):
            return
        currentLetter = lettersList[idx]
        if currentLetter != "":
            currentCount = countOccurrences(currentLetter, lettersList, 0, 0)
            if currentCount > maxFreq:
                maxFreq = currentCount
        findMaxFrequency(idx + 1)

    findMaxFrequency(0)

    def fillDict(idx: int) -> None:
        if idx >= len(lettersList):
            return
        currentLetter = lettersList[idx]
        countLetter = countOccurrences(currentLetter, lettersList, 0, 0)
        if countLetter == maxFreq:
            freqDict[currentLetter] = maxFreq
        fillDict(idx + 1)

    if maxFreq > 0:
        fillDict(0)

    return freqDict