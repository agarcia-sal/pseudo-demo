from typing import List

def filter_by_prefix(listOfStrings: List[str], prefixString: str) -> List[str]:
    resultList: List[str] = []
    currentIndex: int = 0

    while currentIndex < len(listOfStrings):
        candidate: str = listOfStrings[currentIndex]
        if candidate.startswith(prefixString):
            resultList.append(candidate)
        currentIndex += 1

    return resultList