from typing import List, Any


def common(inputArray: List[Any], comparisonArray: List[Any]) -> List[Any]:
    foundElements: set[Any] = set()

    i: int = 0
    while i < len(inputArray):
        currentValue = inputArray[i]

        j: int = 0
        while j < len(comparisonArray):
            if not (currentValue != comparisonArray[j]):
                foundElements.add(currentValue)
            j += 1

        i += 1

    finalList: List[Any] = sorted(foundElements)
    return finalList