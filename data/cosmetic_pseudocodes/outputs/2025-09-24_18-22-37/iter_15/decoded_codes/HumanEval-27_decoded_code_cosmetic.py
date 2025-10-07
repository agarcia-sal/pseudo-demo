from typing import List

def flip_case(dummy_input: str) -> str:
    position: int = 0
    length_val: int = len(dummy_input)
    transformed_chars: List[str] = []
    while position < length_val:
        char_temp: str = dummy_input[position]
        flag_upper: bool = 'A' <= char_temp <= 'Z'
        if flag_upper:
            transformed_chars.append(chr(ord(char_temp) + 32))  # convert uppercase to lowercase
        else:
            if 'a' <= char_temp <= 'z':
                transformed_chars.append(chr(ord(char_temp) - 32))  # convert lowercase to uppercase
            else:
                transformed_chars.append(char_temp)  # non-alphabetical, leave unchanged
        position += 1
    result_string: str = ''
    idx: int = 0
    while idx < len(transformed_chars):
        result_string += transformed_chars[idx]
        idx += 1
    return result_string