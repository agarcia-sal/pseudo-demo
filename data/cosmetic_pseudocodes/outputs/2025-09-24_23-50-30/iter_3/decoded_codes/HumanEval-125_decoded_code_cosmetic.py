from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    for delimiter in [" ", ","]:
        if delimiter in text:
            if delimiter == " ":
                return text.split()
            else:
                temp_text = text.replace(",", " ")
                return temp_text.split()

    characters = [c for c in text if 'a' <= c <= 'z']
    total = sum((ord(char) % 2) == 0 for char in characters)
    return total