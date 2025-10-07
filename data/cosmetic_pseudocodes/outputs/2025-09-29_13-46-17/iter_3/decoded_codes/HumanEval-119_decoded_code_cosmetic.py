from typing import List

def match_parens(list_of_two_strings: List[str]) -> str:
    def check(stringToVerify: str, currentIndex: int, currentBalance: int) -> bool:
        if currentIndex >= len(stringToVerify):
            return currentBalance == 0

        currentChar = stringToVerify[currentIndex]
        if currentChar not in ('(', ')'):
            return False

        updatedBalance = currentBalance + 1 if currentChar == '(' else currentBalance - 1
        if updatedBalance < 0:
            return False

        return check(stringToVerify, currentIndex + 1, updatedBalance)

    firstConcat = list_of_two_strings[0] + list_of_two_strings[1]
    secondConcat = list_of_two_strings[1] + list_of_two_strings[0]

    if check(firstConcat, 0, 0) or check(secondConcat, 0, 0):
        return "Yes"
    return "No"