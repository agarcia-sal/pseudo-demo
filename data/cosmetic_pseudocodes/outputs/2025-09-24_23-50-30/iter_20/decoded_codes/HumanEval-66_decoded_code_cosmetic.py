from typing import Union

def digitSum(originalData: str) -> int:
    if originalData == "":
        return 0
    accumulator: int = 0
    for element in originalData:
        intermediateValue: int = ord(element) if 'A' <= element <= 'Z' else 0
        accumulator += intermediateValue
    return accumulator