from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    def helper_a(chars: List[str], idx: int, acc: int) -> int:
        if idx >= len(chars):
            return acc
        curr_char = chars[idx]
        if 'a' <= curr_char <= 'z':
            curr_code = ord(curr_char)
            if curr_code % 2 == 0:
                return helper_a(chars, idx + 1, acc + 1)
            else:
                return helper_a(chars, idx + 1, acc)
        else:
            return helper_a(chars, idx + 1, acc)

    if text.find(' ') != -1:
        return text.split(' ')
    elif text.find(',') != -1:
        replaced_string = text.replace(',', ' ')
        return replaced_string.split(' ')
    else:
        character_list = list(text)
        return helper_a(character_list, 0, 0)