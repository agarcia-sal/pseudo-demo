from typing import List


def concatenate(listOfStrings: List[str]) -> str:
    startedString = ""
    indexCounter = 0

    while indexCounter < len(listOfStrings):
        startedString += listOfStrings[indexCounter]
        indexCounter += 1

    return startedString