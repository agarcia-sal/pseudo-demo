from typing import Optional


def is_palindrome(word: str) -> bool:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return word == reversed_word


def make_palindrome(original_text: str) -> str:
    if len(original_text) == 0:
        return ""

    index_starting_palindromic_part = 0
    while True:
        current_substring = original_text[index_starting_palindromic_part:]
        if is_palindrome(current_substring):
            break
        index_starting_palindromic_part += 1

    prefix_substring = original_text[:index_starting_palindromic_part]
    prefix_reversed = ""
    for j in range(len(prefix_substring) - 1, -1, -1):
        prefix_reversed += prefix_substring[j]

    return original_text + prefix_reversed