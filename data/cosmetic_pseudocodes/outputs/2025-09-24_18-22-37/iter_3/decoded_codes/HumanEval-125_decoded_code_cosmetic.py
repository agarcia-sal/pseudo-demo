from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    else:
        if "," in text:
            altered_text = []
            for ch in text:
                altered_text.append(" " if ch == "," else ch)
            return "".join(altered_text).split()
        else:
            chars_list = [ch for ch in text]
            total = 0
            for ch in chars_list:
                if ch.islower() and (ord(ch) % 2) == 0:
                    total += 1
            return total