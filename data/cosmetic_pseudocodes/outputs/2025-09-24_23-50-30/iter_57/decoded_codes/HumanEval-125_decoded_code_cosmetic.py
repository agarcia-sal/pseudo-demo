from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    has_space_char: bool = False
    for char in input_string:
        if char == ' ':
            has_space_char = True
            break
    if has_space_char:
        return input_string.split()
    else:
        has_comma_char: bool = False
        for char in input_string:
            if char == ',':
                has_comma_char = True
                break
        if has_comma_char:
            temp_string: str = ''
            index: int = 0
            length: int = len(input_string)
            while index < length:
                if input_string[index] == ',':
                    temp_string += ' '
                else:
                    temp_string += input_string[index]
                index += 1
            return temp_string.split()
        else:
            counter: int = 0
            pos: int = 0
            length = len(input_string)
            while pos < length:
                current_char = input_string[pos]
                if current_char.islower() and (ord(current_char) % 2) == 0:
                    counter += 1
                pos += 1
            return counter