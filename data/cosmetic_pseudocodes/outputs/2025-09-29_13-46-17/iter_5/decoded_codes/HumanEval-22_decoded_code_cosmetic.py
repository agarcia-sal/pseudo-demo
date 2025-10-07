from typing import List, Any

def filter_integers(inputList: List[Any]) -> List[int]:
    resultCollection: List[int] = []
    posIndex: int = 0
    while posIndex < len(inputList):
        currItem = inputList[posIndex]
        if not isinstance(currItem, int):
            posIndex += 1
            continue
        resultCollection.append(currItem)
        posIndex += 1
    return resultCollection