from typing import Union

def multiply(numX: int, numY: int) -> int:
    partOne: int = 0
    partTwo: int = 0

    partOne = abs(numX % 10)
    partTwo = abs(numY % 10)

    return partOne * partTwo