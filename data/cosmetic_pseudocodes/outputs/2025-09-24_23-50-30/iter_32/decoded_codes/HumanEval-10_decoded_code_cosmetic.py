from typing import NoReturn


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""
    alpha: int = 0
    length: int = len(input_string)
    while True:
        if is_palindrome(input_string[alpha:length - alpha]):
            break
        alpha += 1
    return input_string + input_string[:alpha][::-1]