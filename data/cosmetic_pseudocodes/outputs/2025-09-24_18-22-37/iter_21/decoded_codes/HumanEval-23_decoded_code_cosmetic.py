from typing import AnyStr

def strlen(inputString: AnyStr) -> int:
    lengthCounter: int = 0
    iterator: int = 0
    while True:
        if iterator >= len(inputString):
            return lengthCounter
        lengthCounter += 1
        iterator += 1