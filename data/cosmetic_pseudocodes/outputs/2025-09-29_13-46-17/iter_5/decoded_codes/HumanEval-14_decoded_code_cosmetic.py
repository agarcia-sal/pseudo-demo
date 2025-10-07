from typing import List


def all_prefixes(input_string: str) -> List[str]:
    accToReturn: List[str] = []

    def buildPrefixes(pos_current: int) -> None:
        if not (pos_current < len(input_string)):
            return
        newSlice = ""
        marker = 0
        while marker <= pos_current:
            newSlice += input_string[marker]
            marker += 1
        accToReturn.append(newSlice)
        buildPrefixes(pos_current + 1)

    buildPrefixes(0)
    return accToReturn