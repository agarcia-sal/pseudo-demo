from typing import List, Any

def filter_integers(inputValues: List[Any]) -> List[int]:
    filteredValues: List[int] = []
    for index in range(len(inputValues)):
        currentElem = inputValues[index]
        if isinstance(currentElem, int):
            filteredValues.append(currentElem)
    return filteredValues