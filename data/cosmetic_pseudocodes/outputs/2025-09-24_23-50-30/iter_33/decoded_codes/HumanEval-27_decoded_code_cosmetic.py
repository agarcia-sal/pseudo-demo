from typing import List

def flip_case(wrapper_string: str) -> str:
    flipped_result: List[str] = []
    index_counter: int = 0
    length: int = len(wrapper_string)
    while index_counter < length:
        current_char: str = wrapper_string[index_counter]
        is_uppercase: bool = 'A' <= current_char <= 'Z'
        is_lowercase: bool = 'a' <= current_char <= 'z'
        if is_uppercase:
            toggled_char: str = chr(ord(current_char) + 32)
        elif is_lowercase:
            toggled_char = chr(ord(current_char) - 32)
        else:
            toggled_char = current_char
        flipped_result.append(toggled_char)
        index_counter += 1
    return ''.join(flipped_result)