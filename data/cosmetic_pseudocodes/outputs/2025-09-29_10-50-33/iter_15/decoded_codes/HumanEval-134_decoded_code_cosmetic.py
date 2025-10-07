from typing import List


def check_if_last_char_is_a_letter(input_str: str) -> bool:
    index_tracker: int = 0
    word_collection: List[str] = []

    while index_tracker < len(input_str):
        temp_char: str = input_str[index_tracker]
        if temp_char != ' ':
            if len(word_collection) > 0:
                word_collection[-1] += temp_char
            else:
                word_collection.append(temp_char)
        else:
            if len(word_collection) == 0 or word_collection[-1] == '':
                word_collection.append('')
        index_tracker += 1

    extracted_word: str = ''
    if len(word_collection) != 0:
        extracted_word = word_collection[-1]

    char_check: str = extracted_word[0] if len(extracted_word) == 1 else ''
    is_alpha_flag: bool = False

    # Emulate do-while by a single-pass conditional block
    if len(extracted_word) == 1:
        ascii_val: int = ord(char_check.lower())
        if 97 <= ascii_val <= 122:
            is_alpha_flag = True

    return is_alpha_flag