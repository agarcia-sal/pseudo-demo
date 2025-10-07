from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split(" ")
    elif "," in text:
        temp_string = " ".join(text.split(","))
        return temp_string.split(" ")
    else:
        def count_chars(index: int, tally: int) -> int:
            if index >= len(text):
                return tally
            ch = text[index]
            # Check if ch is lowercase letter and its ASCII code is even
            if "a" <= ch <= "z" and (ord(ch) % 2 == 0):
                return count_chars(index + 1, tally + 1)
            else:
                return count_chars(index + 1, tally)
        return count_chars(0, 0)