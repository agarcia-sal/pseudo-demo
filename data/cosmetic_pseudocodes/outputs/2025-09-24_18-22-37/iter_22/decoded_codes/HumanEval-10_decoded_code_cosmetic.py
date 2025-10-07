from typing import Optional


def is_palindrome(candidate_string: str) -> bool:
    reversed_version = ""
    index_counter = len(candidate_string) - 1

    while index_counter >= 0:
        reversed_version += candidate_string[index_counter]
        index_counter -= 1

    return candidate_string == reversed_version


def make_palindrome(source_string: str) -> str:
    if len(source_string) == 0:
        return ""

    suffix_start_position = 0
    palindrome_suffix_found = False

    while not palindrome_suffix_found:
        test_substring = ""
        i = suffix_start_position

        while i < len(source_string):
            test_substring += source_string[i]
            i += 1

        if is_palindrome(test_substring):
            palindrome_suffix_found = True
        else:
            suffix_start_position += 1

    prefix_to_append = ""
    j = 0

    while j < suffix_start_position:
        prefix_to_append = source_string[j] + prefix_to_append
        j += 1

    return source_string + prefix_to_append