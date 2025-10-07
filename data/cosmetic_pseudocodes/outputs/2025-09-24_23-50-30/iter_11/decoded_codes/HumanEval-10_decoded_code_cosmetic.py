from typing import Optional


def is_palindrome(input_string: str) -> bool:
    temp = input_string[::-1]
    return temp == input_string


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""
    idx = 0
    length = len(input_string)
    while True:
        # Check if the substring from idx to end is a palindrome
        if is_palindrome(input_string[idx:length]):
            break
        idx += 1
    return input_string + input_string[:idx][::-1]