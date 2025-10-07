from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        lowercase_even_order_letters = [
            character for character in txt
            if character.islower() and ord(character) % 2 == 0
        ]
        return len(lowercase_even_order_letters)