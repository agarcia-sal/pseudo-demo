from typing import List


def string_sequence(integer_n: int) -> str:
    resultList: List[str] = []
    index: int = 0
    while index <= integer_n:
        resultList.append(str(index))
        index += 1

    outputString: str = ""
    i: int = 0
    while i < len(resultList):
        if i == len(resultList) - 1:
            outputString += resultList[i]
        else:
            outputString += resultList[i] + " "
        i += 1

    return outputString