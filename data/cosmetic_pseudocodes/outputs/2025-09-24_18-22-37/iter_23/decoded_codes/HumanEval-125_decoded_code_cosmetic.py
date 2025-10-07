from typing import Union, List


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split(" ")
    else:
        if "," in input_string:
            intermediate_string: str = input_string.replace(",", " ")
            return intermediate_string.split(" ")
        else:
            character_list: List[str] = list(input_string)
            lowercase_characters: List[str] = []
            iterator_index: int = 0
            while iterator_index < len(character_list):
                current_char: str = character_list[iterator_index]
                if current_char.islower() and (ord(current_char) % 2 == 0):
                    lowercase_characters.append(current_char)
                iterator_index += 1
            lowercase_count: int = len(lowercase_characters)
            return lowercase_count