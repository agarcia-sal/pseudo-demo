from typing import Dict


def encode(originalMessage: str) -> str:
    vowelsString: str = "AEIOUaeiou"
    vowelsMapping: Dict[str, str] = {}

    def buildMapping(index: int) -> None:
        if index == len(vowelsString):
            return
        currentChar = vowelsString[index]
        mappedChar = chr(ord(currentChar) + 2)
        vowelsMapping[currentChar] = mappedChar
        buildMapping(index + 1)

    buildMapping(0)

    swappedMessage_chars: list[str] = []

    def swapCase(position: int) -> None:
        if position == len(originalMessage):
            return
        c = originalMessage[position]
        if 'a' <= c <= 'z':
            swappedMessage_chars.append(c.upper())
        elif 'A' <= c <= 'Z':
            swappedMessage_chars.append(c.lower())
        else:
            swappedMessage_chars.append(c)
        swapCase(position + 1)

    swapCase(0)
    swappedMessage = "".join(swappedMessage_chars)

    finalString_chars: list[str] = []

    def replaceVowelsAgainstMap(pos: int) -> None:
        if pos == len(swappedMessage):
            return
        ch = swappedMessage[pos]
        if ch in vowelsMapping:
            finalString_chars.append(vowelsMapping[ch])
        else:
            finalString_chars.append(ch)
        replaceVowelsAgainstMap(pos + 1)

    replaceVowelsAgainstMap(0)

    return "".join(finalString_chars)