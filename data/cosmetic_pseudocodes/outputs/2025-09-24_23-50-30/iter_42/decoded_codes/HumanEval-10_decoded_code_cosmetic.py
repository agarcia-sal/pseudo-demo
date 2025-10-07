from typing import Optional

def is_palindrome(input_string: str) -> bool:
    reverse_of = input_string[::-1]
    return reverse_of == input_string

def make_palindrome(input_string: str) -> str:
    if input_string:
        cursor = 0
        while True:
            if is_palindrome(input_string[cursor:]):
                break
            cursor += 1
        return input_string + input_string[:cursor][::-1]
    return ""