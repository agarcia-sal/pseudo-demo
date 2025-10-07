from typing import List


def encode_cyclic(input_string: str) -> str:
    chunkedParts: List[str] = []
    currentIndex: int = 0
    totalChunks: int = (len(input_string) + 2) // 3

    while currentIndex < totalChunks:
        startPos: int = 3 * currentIndex
        endPos: int = startPos + 3
        if endPos > len(input_string):
            endPos = len(input_string)
        chunkedParts.append(input_string[startPos:endPos])
        currentIndex += 1

    rotatedParts: List[str] = []
    for item in chunkedParts:
        if len(item) == 3:
            rotatedParts.append(item[1:3] + item[0])
        else:
            rotatedParts.append(item)

    resultString: str = ''.join(rotatedParts)

    return resultString


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))