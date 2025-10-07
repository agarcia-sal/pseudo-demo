from typing import Set, Dict

def encode(inputString: str) -> str:
    validVowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    shiftMap: Dict[str, str] = {
        letter: chr(ord(letter) + 2)
        for letter in validVowels
    }

    resultList: list[str] = [
        shiftMap[symbol] if symbol in validVowels else symbol
        for symbol in inputString.swapcase()
    ]

    return ''.join(resultList)