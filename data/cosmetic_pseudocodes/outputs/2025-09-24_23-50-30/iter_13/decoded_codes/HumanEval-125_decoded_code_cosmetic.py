from typing import Union, List


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        temp_text = text.replace(",", " ")
        return temp_text.split()
    else:
        filtered_chars = [char for char in text if char.islower() and (ord(char) % 2) == 0]
        total_count = len(filtered_chars)
        return total_count