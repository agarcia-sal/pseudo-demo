from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        parts: List[str] = text.split()
        return parts
    else:
        if "," in text:
            subbed_string = "".join(" " if char == "," else char for char in text)
            return subbed_string.split()
        else:
            total_even_lowercase = 0
            index = 0
            while index < len(text):
                current_char = text[index]
                if "a" <= current_char <= "z" and (ord(current_char) % 2 == 0):
                    total_even_lowercase += 1
                index += 1
            return total_even_lowercase