from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    def helper_replace(commas_list: List[str], idx: int, length: int, output_list: List[str]) -> List[str]:
        if idx < length:
            output_list[idx] = ' ' if commas_list[idx] == ',' else commas_list[idx]
            return helper_replace(commas_list, idx + 1, length, output_list)
        else:
            return output_list

    def helper_count_lower_ascii(char_seq: List[str], pos: int, total_length: int, acc: int) -> int:
        if pos < total_length:
            current_char = char_seq[pos]
            is_lowercase_flag = 'a' <= current_char <= 'z'
            ascii_val = ord(current_char)
            condition_flag = (ascii_val % 2 == 0)
            acc += 1 if is_lowercase_flag and condition_flag else 0
            return helper_count_lower_ascii(char_seq, pos + 1, total_length, acc)
        else:
            return acc

    if ' ' in input_string:
        return input_string.split()
    elif ',' in input_string:
        chars_array = list(input_string)
        replaced_chars = helper_replace(chars_array, 0, len(chars_array), [''] * len(chars_array))
        replaced_string = ''.join(replaced_chars)
        return replaced_string.split()
    else:
        chars_seq = list(input_string)
        return helper_count_lower_ascii(chars_seq, 0, len(chars_seq), 0)