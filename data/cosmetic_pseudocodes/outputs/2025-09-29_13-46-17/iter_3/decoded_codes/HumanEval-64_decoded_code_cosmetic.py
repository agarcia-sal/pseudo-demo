from typing import List


def vowels_count(inputString: str) -> int:
    vowelChars = "aeiouAEIOU"

    def countVowelsRecursive(charsList: List[str], acc: int) -> int:
        if not charsList:
            return acc
        currentChar = charsList[0]
        restChars = charsList[1:]
        added = 1 if currentChar in vowelChars else 0
        return countVowelsRecursive(restChars, acc + added)

    vowelsFound = countVowelsRecursive(list(inputString), 0)

    if not (inputString[-1] != 'y' and inputString[-1] != 'Y'):
        return vowelsFound + 1
    return vowelsFound