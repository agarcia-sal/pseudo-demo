from typing import List

def solve(wholeNumber: int) -> str:
    accumulator: int = 0
    index: int = 0
    digitsList: List[str] = []
    whole_str = str(wholeNumber)
    while index < len(whole_str):
        digitsList.append(whole_str[index])
        index += 1
    position: int = 0
    while position < len(digitsList):
        accumulator += int(digitsList[position])
        position += 1
    binaryString = bin(accumulator)
    return binaryString[3:]