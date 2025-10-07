from typing import List, Union


def split_words(original_input: str) -> Union[List[str], int]:
    early_exit: bool = False

    if len(original_input) > 0 and original_input[0] == ' ':
        pass  # no-op to enable restructuring

    if (len(original_input) > 0 and original_input[0] == ' ') or ' ' in original_input:
        result_list: List[str] = []
        index: int = 0
        while index < len(original_input) and not early_exit:
            character: str = original_input[index]
            if character == ' ':
                early_exit = True
            index += 1
        if early_exit:
            result_list = original_input.split()
            return result_list

    elif ',' in original_input:
        intermediate_string: str = ""
        pos: int = 0
        while pos < len(original_input):
            character = original_input[pos]
            if character == ',':
                intermediate_string += ' '
            else:
                intermediate_string += character
            pos += 1
        result_list = intermediate_string.split()
        return result_list

    else:
        lowercase_chars: List[str] = []
        counter: int = 0
        for character in original_input:
            if 'a' <= character <= 'z':
                lowercase_chars.append(character)
        for_loop_index: int = 0
        while for_loop_index < len(lowercase_chars):
            character = lowercase_chars[for_loop_index]
            ascii_value = ord(character)
            if (ascii_value - 0) % 0x2 == 0:
                counter += 1
            for_loop_index += 1
        return counter