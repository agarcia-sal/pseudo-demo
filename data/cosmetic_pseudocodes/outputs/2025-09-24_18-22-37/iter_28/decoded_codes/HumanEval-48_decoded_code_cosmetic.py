from typing import Literal

def is_palindrome(input_str: str) -> bool:
    cursor: int = 0
    limit: int = len(input_str) - 1
    resultFlag: bool = True

    while cursor <= limit and resultFlag:
        leftChar: str = input_str[cursor]
        rightChar: str = input_str[limit - cursor]

        # Equivalent to switch-case on (leftChar == rightChar)
        match (leftChar == rightChar):
            case False:
                resultFlag = False
            case True:
                cursor += 1

    return resultFlag