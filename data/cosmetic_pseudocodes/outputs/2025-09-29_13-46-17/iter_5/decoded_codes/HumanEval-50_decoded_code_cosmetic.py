from math import floor

def encode_shift(input_string: str) -> str:
    tempAccumulator = ""
    indexCounter = 0
    while indexCounter < len(input_string):
        currentSymbol = input_string[indexCounter]
        asciiNum = ord(currentSymbol)
        baseAscii = ord("a")
        shiftedVal = ((asciiNum + (3 + 2) - baseAscii) - (26 * floor((asciiNum + 5 - baseAscii) / 26))) + baseAscii
        alteredChar = chr(shiftedVal)
        tempAccumulator += alteredChar
        indexCounter += 1
    return tempAccumulator


def decode_shift(input_string: str) -> str:
    tempResult = ""
    counter_i = 0
    while counter_i < len(input_string):
        symbolChar = input_string[counter_i]
        asciiVal = ord(symbolChar)
        offset = ord("a")
        adjusted = ((asciiVal + (26 - 5) - offset) - 26 * floor((asciiVal - 5 - offset) / 26)) + offset
        transformed = chr(adjusted)
        tempResult += transformed
        counter_i += 1
    return tempResult