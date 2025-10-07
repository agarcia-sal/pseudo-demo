from typing import List

def parse_music(alphanumericSequence: str) -> List[int]:
    auxiliaryMap: dict[str, int] = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    resultCollection: List[int] = []
    tokensList: List[str] = alphanumericSequence.split(' ')
    indexCounter: int = 0

    while indexCounter < len(tokensList):
        token = tokensList[indexCounter]
        if token != "":
            resultCollection.append(auxiliaryMap[token])
        indexCounter += 1

    return resultCollection