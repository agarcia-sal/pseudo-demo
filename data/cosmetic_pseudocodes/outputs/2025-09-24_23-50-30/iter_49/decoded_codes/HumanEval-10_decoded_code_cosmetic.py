from typing import Callable


def is_palindrome(coded_input: str) -> bool:
    return coded_input == coded_input[::-1]


def make_palindrome(encoded_word: str) -> str:
    def seek_suffix(index_counter: int) -> int:
        if index_counter >= len(encoded_word):
            return index_counter
        elif not is_palindrome(encoded_word[index_counter:]):
            return seek_suffix(index_counter + 1)
        else:
            return index_counter

    if len(encoded_word) == 0:
        return ""
    suffix_index = seek_suffix(0)
    return encoded_word + encoded_word[:suffix_index][::-1]