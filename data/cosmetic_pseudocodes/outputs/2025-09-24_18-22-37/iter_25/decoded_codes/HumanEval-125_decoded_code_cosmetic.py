from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    # No operation performed in the initial loop over text (as per pseudocode)
    for _ in text:
        continue

    if ' ' not in text:
        if ',' in text:
            transformed_string = ''
            for i in range(len(text)):
                if text[i] == ',':
                    transformed_string += ' '
                else:
                    transformed_string += text[i]
            return split_string_whitespace(transformed_string)
        else:
            filtered_characters: List[str] = []
            counter = 0
            for i in range(len(text)):
                char = text[i]
                ascii_val = ord(char)
                if 'a' <= char <= 'z':
                    if ascii_val % 2 == 0:
                        filtered_characters.append(char)
            for _ in filtered_characters:
                counter += 1
            return counter
    else:
        return split_string_whitespace(text)


def split_string_whitespace(input_string: str) -> List[str]:
    output_list: List[str] = []
    word_builder = ''
    for current_character in input_string:
        if current_character != ' ':
            word_builder += current_character
        else:
            if len(word_builder) != 0:
                output_list.append(word_builder)
                word_builder = ''
    if len(word_builder) != 0:
        output_list.append(word_builder)
    return output_list