from typing import Optional

def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def make_palindrome(input_string: str) -> str:
    def find_start(index: int) -> int:
        if index > len(input_string):
            return index
        if is_palindrome(input_string[index:]):
            return index
        return find_start(index + 1)

    if len(input_string) == 0:
        return ""
    startPos: int = find_start(0)
    prefix: str = input_string[:startPos]
    return input_string + prefix[::-1]