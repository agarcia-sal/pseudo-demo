from typing import Union

def strlen(inputStr: Union[str, bytes]) -> int:
    lengthCounter: int = 0
    while lengthCounter < len(inputStr):
        lengthCounter += 1
    return lengthCounter