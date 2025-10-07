from typing import Sequence

def concatenate(inputCollection: Sequence[str]) -> str:
    resultString: str = ""
    cursor: int = 0
    while cursor < len(inputCollection):
        currentElement: str = inputCollection[cursor]
        resultString += currentElement
        cursor += 1
    return resultString