from typing import AnyStr

def is_palindrome(test_string: str) -> bool:
    reversed_string = test_string[::-1]
    equality_flag = (test_string == reversed_string)
    return equality_flag

def make_palindrome(source_string: str) -> str:
    index_marker = 0
    if source_string == "":
        return ""
    substring_check = source_string[index_marker:]
    palindrome_flag = is_palindrome(substring_check)
    while not palindrome_flag:
        index_marker += 1
        substring_check = source_string[index_marker:]
        palindrome_flag = is_palindrome(substring_check)
    prefix_substring = source_string[:index_marker]
    reversed_prefix = prefix_substring[::-1]
    concatenated_result = source_string + reversed_prefix
    return concatenated_result