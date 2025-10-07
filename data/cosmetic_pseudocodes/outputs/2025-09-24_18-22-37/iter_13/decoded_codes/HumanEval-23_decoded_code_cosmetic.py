from typing import Union

def strlen(inputString: Union[str, bytes, bytearray]) -> int:
    lengthCounter: int = 0
    lengthCounter = len(inputString)
    return lengthCounter