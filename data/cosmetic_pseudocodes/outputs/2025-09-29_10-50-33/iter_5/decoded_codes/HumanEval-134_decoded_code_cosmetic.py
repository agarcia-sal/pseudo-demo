from typing import List


def check_if_last_char_is_a_letter(input_string: str) -> bool:
    def is_ascii_lowercase(character: str) -> bool:
        return 97 <= ord(character) <= 122

    list_of_words: List[str] = input_string.split(" ")
    last_token_index: int = len(list_of_words) - 1

    if last_token_index < 0:
        return False

    last_token: str = list_of_words[last_token_index]
    if len(last_token) == 1:
        return is_ascii_lowercase(last_token.lower())
    else:
        return False