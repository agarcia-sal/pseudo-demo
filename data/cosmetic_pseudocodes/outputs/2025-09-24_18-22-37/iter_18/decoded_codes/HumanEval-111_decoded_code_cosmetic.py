from typing import Dict

def histogram(cBrick: str) -> Dict[str, int]:
    freqMap: Dict[str, int] = {}
    splitTokens = cBrick.split(' ')

    peakFreq = 0
    idx = 0

    while idx < len(splitTokens):
        currentToken = splitTokens[idx]
        currentCount = 0
        for element in splitTokens:
            if element == currentToken:
                currentCount += 1
        if currentCount > peakFreq and currentToken != '':
            peakFreq = currentCount
        idx += 1

    if peakFreq <= 0:
        return freqMap

    j = 0
    while j < len(splitTokens):
        tokenLoop = splitTokens[j]
        countLoop = 0

        for element in splitTokens:
            if element == tokenLoop:
                countLoop += 1

        if countLoop == peakFreq:
            freqMap[tokenLoop] = peakFreq

        j += 1

    return freqMap