from typing import List

def concatenate(array_of_texts: List[str]) -> str:
    resultText: str = ""
    index: int = 0

    while index < len(array_of_texts):
        resultText += array_of_texts[index]
        index += 1

    return resultText