from typing import List, Union


def split_words(message: str) -> Union[List[str], int]:
    if " " in message:
        word_list: List[str] = message.split()
        return word_list
    else:
        if "," in message:
            interim_string: str = message.replace(",", " ")
            tokens: List[str] = interim_string.split()
            return tokens
        else:
            character_collection: List[str] = list(message)
            filtered_chars: List[str] = []
            index_var: int = 0
            while index_var < len(character_collection):
                current_char: str = character_collection[index_var]
                is_lowercase: bool = current_char.islower()
                char_ascii_value: int = ord(current_char)
                even_ascii_condition: bool = (char_ascii_value % 2) == 0
                if is_lowercase and even_ascii_condition:
                    filtered_chars.append(current_char)
                index_var += 1
            result_count: int = len(filtered_chars)
            return result_count