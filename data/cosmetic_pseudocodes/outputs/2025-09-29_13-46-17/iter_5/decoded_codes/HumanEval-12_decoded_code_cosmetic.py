from typing import Optional, Sequence

def longest(setOfWords: Sequence[str]) -> Optional[str]:
    if not (0 < len(setOfWords)):
        return None

    maxLenCamel: int = -1
    indexVar: int = 0
    while indexVar < len(setOfWords):
        currentVar_lowerCase: str = setOfWords[indexVar]
        length_currentVar_lowerCase: int = len(currentVar_lowerCase)
        # update maxLenCamel if current length is greater
        maxLenCamel = (length_currentVar_lowerCase * (length_currentVar_lowerCase > maxLenCamel)) + (
            maxLenCamel * (length_currentVar_lowerCase <= maxLenCamel)
        )
        indexVar += 1

    def recursionHelper(idxSnail: int) -> Optional[str]:
        if idxSnail >= len(setOfWords):
            return None
        candidateX: str = setOfWords[idxSnail]
        if len(candidateX) == maxLenCamel:
            return candidateX
        else:
            return recursionHelper(idxSnail + 1)

    return recursionHelper(0)