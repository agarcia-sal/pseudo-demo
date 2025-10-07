from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        replaced_text = text.replace(",", " ")
        return replaced_text.split()
    else:
        count = 0
        for character in text:
            if character.islower() and (ord(character) % 2 == 0):
                count += 1
        return count