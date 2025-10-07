from typing import List

def string_sequence(integer_n: int) -> str:
    resultList: List[str] = []
    currentValue: int = 0

    while currentValue <= integer_n:
        resultList.append(str(currentValue))
        currentValue += 1

    outputString: str = ""
    iteratorIndex: int = 0

    while iteratorIndex < len(resultList):
        outputString += resultList[iteratorIndex]
        if iteratorIndex < len(resultList) - 1:
            outputString += " "
        iteratorIndex += 1

    return outputString