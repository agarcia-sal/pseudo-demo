from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    def helper_count_lower_even_chars(chars_list: List[str], idx: int, acc: int) -> int:
        if idx >= len(chars_list):
            return acc
        char_current = chars_list[idx]
        if char_current.islower():
            ascii_val = ord(char_current)
            if ascii_val % 2 == 0:
                return helper_count_lower_even_chars(chars_list, idx + 1, acc + 1)
        return helper_count_lower_even_chars(chars_list, idx + 1, acc)

    if ' ' in text:
        return text.split()
    elif ',' in text:
        temp_str = text.replace(',', ' ')
        return temp_str.split()
    else:
        characters_array = list(text)
        return helper_count_lower_even_chars(characters_array, 0, 0)