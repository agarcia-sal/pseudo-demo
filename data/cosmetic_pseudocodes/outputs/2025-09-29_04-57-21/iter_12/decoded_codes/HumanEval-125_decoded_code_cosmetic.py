from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    if "," in text:
        replaced_string = []
        for char in text:
            if char == ",":
                replaced_string.append(" ")
            else:
                replaced_string.append(char)
        return "".join(replaced_string).split()
    filtered_chars = [char for char in text if 'a' <= char <= 'z' and (ord(char) % 2 == 0)]
    return len(filtered_chars)