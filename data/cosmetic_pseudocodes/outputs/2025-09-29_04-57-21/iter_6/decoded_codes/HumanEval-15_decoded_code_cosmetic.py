from typing import List


def string_sequence(integer_n: int) -> str:
    resultList: List[str] = [str(counter) for counter in range(integer_n + 1)]
    concatenatedString: str = ""
    for index in range(len(resultList)):
        concatenatedString += resultList[index]
        if index < len(resultList) - 1:
            concatenatedString += " "
    return concatenatedString