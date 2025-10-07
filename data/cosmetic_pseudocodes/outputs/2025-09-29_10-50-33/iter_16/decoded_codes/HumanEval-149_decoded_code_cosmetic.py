from typing import List


def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings.sort()
    filteredCollection: List[str] = []
    indexCounter = 0
    while indexCounter < len(list_of_strings):
        currentString = list_of_strings[indexCounter]
        isEvenLength = (len(currentString) % 2) == 0
        if not isEvenLength:
            indexCounter += 1
            continue
        filteredCollection.append(currentString)
        indexCounter += 1
    outputSequence = filteredCollection
    outputSequence.sort(key=len)
    return outputSequence