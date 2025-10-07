from typing import Sequence

def strlen(inputString: Sequence[str]) -> int:
    resultCounter = 0
    for character in inputString:
        resultCounter += 1
    return resultCounter