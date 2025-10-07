from typing import Optional


def is_palindrome(input_string: str) -> bool:
    fCount: int = len(input_string) - 1
    rCount: int = 0
    while fCount >= rCount:
        if input_string[fCount] != input_string[rCount]:
            return False
        fCount -= 1
        rCount += 1
    return True


def make_palindrome(input_string: str) -> str:
    L_s: int = len(input_string)
    if L_s == 0:
        return ""

    def seek_start(index: int) -> int:
        if index == L_s:
            return L_s
        subStr: str = input_string[index:L_s]
        if is_palindrome(subStr):
            return index
        return seek_start(index + 1)

    pos: int = seek_start(0)
    prefix: str = input_string[0:pos]
    reversed_prefix: str = "".join(prefix[i] for i in range(len(prefix) - 1, -1, -1))

    return input_string + reversed_prefix