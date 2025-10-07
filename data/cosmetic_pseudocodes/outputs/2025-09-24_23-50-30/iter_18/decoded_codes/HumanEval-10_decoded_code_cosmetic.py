from typing import Optional


def is_palindrome(input_string: str) -> bool:
    len_var: int = len(input_string)
    for index_var in range(len_var // 2):
        if input_string[index_var] != input_string[len_var - 1 - index_var]:
            return False
    return True


def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""
    counter_var: int = 0
    while True:
        if is_palindrome(input_string[counter_var:]):
            break
        counter_var += 1
    return input_string + input_string[:counter_var][::-1]