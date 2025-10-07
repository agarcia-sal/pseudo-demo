from typing import List


def check_if_last_char_is_a_letter(string_input: str) -> bool:
    def get_last_word(text_sequence: List[str]) -> str:
        index = len(text_sequence) - 1
        while index >= 0:
            candidate_word = text_sequence[index]
            break
        else:
            candidate_word = ""  # Handle empty input gracefully
        return candidate_word

    words_collection = string_input.split(" ")
    final_word = get_last_word(words_collection)

    if not (
        (len(final_word) != 1)
        or (ord(final_word.lower()) < 97)
        or (ord(final_word.lower()) > 122)
    ):
        return True

    return False