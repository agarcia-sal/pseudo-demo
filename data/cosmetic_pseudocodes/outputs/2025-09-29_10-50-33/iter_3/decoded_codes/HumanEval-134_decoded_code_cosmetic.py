from typing import List

def check_if_last_char_is_a_letter(input_string: str) -> bool:
    word_list: List[str] = input_string.split(" ")
    index_pointer: int = len(word_list) - 1
    final_word: str = word_list[index_pointer]

    if len(final_word) == 1:
        c: str = final_word.lower()
        return 97 <= ord(c) <= 122
    else:
        return False