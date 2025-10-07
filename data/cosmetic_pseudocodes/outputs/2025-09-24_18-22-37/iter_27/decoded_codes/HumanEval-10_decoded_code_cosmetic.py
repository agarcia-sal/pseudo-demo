from typing import Optional


def is_palindrome(input_string: str) -> bool:
    temporary_variable: str = input_string[::-1]
    comparison_result: bool = input_string == temporary_variable
    return comparison_result


def make_palindrome(input_string: str) -> str:
    if input_string:
        index_tracker: int = 0
        length: int = len(input_string)
        while True:
            sub_str: str = input_string[index_tracker:length]
            if is_palindrome(sub_str):
                break
            index_tracker += 1

        prefix_substring: str = input_string[0:index_tracker]
        reversed_prefix: str = prefix_substring[::-1]
        result: str = input_string + reversed_prefix
        return result
    else:
        return ""