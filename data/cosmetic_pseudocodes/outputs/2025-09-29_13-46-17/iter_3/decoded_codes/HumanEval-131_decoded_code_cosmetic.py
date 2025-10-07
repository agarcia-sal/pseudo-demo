from typing import List

def digits(n: int) -> int:
    def recurseCharacters(characters: str, accProduct: int, accOddCount: int) -> int:
        if not characters:
            return accProduct if accOddCount != 0 else 0

        currentChar = characters[0]
        remainingChars = characters[1:]
        digitValue = int(currentChar)

        if digitValue % 2 != 0:
            newProduct = accProduct * digitValue
            newOddCount = accOddCount + 1
            return recurseCharacters(remainingChars, newProduct, newOddCount)
        else:
            return recurseCharacters(remainingChars, accProduct, accOddCount)

    return recurseCharacters(str(n), 1, 0)