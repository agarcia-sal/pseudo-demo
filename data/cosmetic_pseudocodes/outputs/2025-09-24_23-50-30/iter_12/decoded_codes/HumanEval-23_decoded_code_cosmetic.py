from typing import Sequence

def strlen(inputData: Sequence) -> int:
    counter: int = 0
    while True:
        if counter == len(inputData):
            break
        counter += 1
    return counter