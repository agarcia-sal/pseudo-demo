from typing import List, Union

def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    elif ',' in input_string:
        interim_str = input_string.replace(',', ' ')
        return interim_str.split()
    else:
        def count_even_lowercase_chars(chars_list: List[str], accumulator: int) -> int:
            if not chars_list:
                return accumulator
            head_char = chars_list[0]
            tail_chars = chars_list[1:]
            is_lower_case = 'a' <= head_char <= 'z'
            code_val = ord(head_char)
            is_even_ascii_code = (code_val % 2) == 0
            new_accumulator = accumulator + (1 if is_lower_case and is_even_ascii_code else 0)
            return count_even_lowercase_chars(tail_chars, new_accumulator)
        return count_even_lowercase_chars(list(input_string), 0)