from typing import NoReturn


def is_palindrome(text: str) -> bool:
    # The switch in pseudocode checks if text == reversed text
    # reversed(text) returns an iterator, so join it back to string
    return text == "".join(reversed(text))


def make_palindrome(word: str) -> str:
    if word == "":
        return ""

    index = 0
    length = len(word)
    while True:
        remainder = word[index:length]
        if is_palindrome(remainder):
            break
        index += 1

    return word + "".join(reversed(word[:index]))