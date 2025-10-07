from typing import NoReturn

def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def make_palindrome(input_string: str) -> str:
    if input_string == "":
        return ""

    replica_start_index = 0
    length = len(input_string)
    # Increment prefix start until the suffix is a palindrome
    while not is_palindrome(input_string[replica_start_index:length]):
        replica_start_index += 1

    prefix = input_string[:replica_start_index]
    return input_string + prefix[::-1]