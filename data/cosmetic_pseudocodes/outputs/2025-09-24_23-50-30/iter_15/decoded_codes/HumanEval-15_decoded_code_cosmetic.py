from typing import List

def string_sequence(integer_n: int) -> str:
    resultContainer: List[str] = []
    iterator: int = 0

    while iterator <= integer_n:
        resultContainer.append(str(iterator))
        iterator += 1

    finalString: str = ""
    index: int = 0

    while True:
        if index >= len(resultContainer):
            break

        if index == 0:
            finalString = resultContainer[index]
        else:
            finalString += " " + resultContainer[index]

        index += 1

    return finalString