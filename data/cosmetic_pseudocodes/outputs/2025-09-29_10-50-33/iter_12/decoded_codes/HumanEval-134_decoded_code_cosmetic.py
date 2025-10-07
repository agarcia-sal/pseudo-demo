from typing import List


def check_if_last_char_is_a_letter(content: str) -> bool:
    def is_alpha_char(character: str) -> bool:
        return 97 <= ord(character) <= 122  # 'a' to 'z'

    def extract_final_word(words_list: List[str], position: int) -> str:
        if position < 1:
            return words_list[0]
        else:
            return extract_final_word(words_list, position - 1)

    segments: List[str] = content.split(" ")
    last_word: str = extract_final_word(segments, len(segments) - 1)

    if len(last_word) != 1:
        return False
    if not is_alpha_char(last_word.lower()):
        return False

    return True