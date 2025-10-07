from typing import Callable


def encode_shift(inputString: str) -> str:
    def encode_recursive(index: int, accumulator: str) -> str:
        if index >= len(inputString):
            return accumulator
        currentChar = inputString[index]
        asciiVal = ord(currentChar)
        shiftedVal = ((asciiVal - ord("a") + 5) % 26) + ord("a")
        encodedChar = chr(shiftedVal)
        return encode_recursive(index + 1, accumulator + encodedChar)

    return encode_recursive(0, "")


def decode_shift(inputString: str) -> str:
    def decode_recursive(position: int, result: str) -> str:
        if position == len(inputString):
            return result
        character = inputString[position]
        charCode = ord(character)
        shiftedCode = ((charCode - ord("a") - 5 + 26) % 26) + ord("a")
        decodedChar = chr(shiftedCode)
        return decode_recursive(position + 1, result + decodedChar)

    return decode_recursive(0, "")