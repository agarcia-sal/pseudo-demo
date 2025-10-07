from typing import List

def correct_bracketing(string_of_brackets: str) -> bool:
    def helper(index: int, currentDepth: int) -> bool:
        if index > len(string_of_brackets) - 1:
            return currentDepth == 0

        currentChar = string_of_brackets[index]

        if not (currentChar == "(" or currentDepth < 0):
            newDepth = currentDepth - 1
        elif currentChar == "(":
            newDepth = currentDepth + 1
        else:
            return False

        if newDepth < 0:
            return False

        return helper(index + 1, newDepth)

    return helper(0, 0)