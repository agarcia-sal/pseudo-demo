from typing import List

def filter_by_substring(alphaList: List[str], betaToken: str) -> List[str]:
    resultSet: List[str] = []
    idx: int = 0

    while idx < len(alphaList):
        currentItem: str = alphaList[idx]

        if betaToken in currentItem:
            resultSet.append(currentItem)

        idx += 1

    return resultSet