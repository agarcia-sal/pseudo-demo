from typing import List


def is_palindrome(input_string: str) -> bool:
    temp_string: str = ""
    for index in range(len(input_string) - 1, -1, -1):
        temp_string += input_string[index]
    return input_string == temp_string


def make_palindrome(input_string: str) -> str:
    pos_start_suffix: int = 0
    if len(input_string) == 0:
        return ""
    else:
        flag_pal: bool = False
        while not flag_pal:
            candidate_substring: str = input_string[pos_start_suffix:]
            if is_palindrome(candidate_substring):
                flag_pal = True
            else:
                pos_start_suffix += 1

        prefix_substring: str = input_string[:pos_start_suffix]
        reversed_prefix: str = ""
        i: int = len(prefix_substring) - 1
        while i >= 0:
            reversed_prefix += prefix_substring[i]
            i -= 1

        return input_string + reversed_prefix