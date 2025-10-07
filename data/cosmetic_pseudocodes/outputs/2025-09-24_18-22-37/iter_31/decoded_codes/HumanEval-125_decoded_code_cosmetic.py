from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        output_value: List[str] = input_string.split()
    else:
        if "," in input_string:
            replaced_chars = [
                " " if ch == "," else ch
                for ch in input_string
            ]
            replaced_string = "".join(replaced_chars)
            output_value = replaced_string.split()
        else:
            letter_list: List[str] = [
                ch for ch in input_string
                if "a" <= ch <= "z" and (ord(ch) % 2) == 0
            ]
            output_value = len(letter_list)
    return output_value