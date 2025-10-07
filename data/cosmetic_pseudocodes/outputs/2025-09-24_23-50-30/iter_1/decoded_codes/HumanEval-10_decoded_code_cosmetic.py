from typing import Sequence

def is_palindrome(input_string: str) -> bool:
    rev_string = ""
    for i in range(len(input_string), 0, -1):
        rev_string += input_string[i - 1]  # i is 1-based in pseudocode; Python is 0-based
    return input_string == rev_string

def make_palindrome(input_string: str) -> str:
    if len(input_string) == 0:
        return ""
    start_index = 0
    while True:
        if is_palindrome(input_string[start_index:]):
            break
        start_index += 1
    prefix = input_string[:start_index]
    suffix = ""
    for j in range(len(prefix), 0, -1):
        suffix += prefix[j - 1]
    return input_string + suffix