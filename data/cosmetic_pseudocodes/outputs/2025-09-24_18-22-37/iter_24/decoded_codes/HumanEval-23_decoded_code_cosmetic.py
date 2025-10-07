from typing import Union

def strlen(inputString: Union[str, bytes]) -> int:
    lengthCounter: int = 0
    while lengthCounter < len(inputString):
        lengthCounter += 1
    return lengthCounter