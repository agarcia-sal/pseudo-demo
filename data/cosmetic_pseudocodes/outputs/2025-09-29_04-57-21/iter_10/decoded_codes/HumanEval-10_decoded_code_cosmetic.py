from typing import Optional


def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]


def make_palindrome(input_string: str) -> str:
    if input_string:
        suffix_start = 0
        length = len(input_string)
        while True:
            tail = input_string[suffix_start:length]
            if is_palindrome(tail):
                break
            suffix_start += 1
        return input_string + input_string[:suffix_start][::-1]
    else:
        return ""