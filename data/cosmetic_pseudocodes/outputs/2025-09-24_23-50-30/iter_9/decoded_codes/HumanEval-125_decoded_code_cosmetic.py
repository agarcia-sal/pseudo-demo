from typing import List, Union


def split_words(str: str) -> Union[List[str], int]:
    if " " in str:
        return str.split()
    elif "," in str:
        tmp_val = str.replace(",", " ")
        return tmp_val.split()
    else:
        # Count lowercase characters with even ASCII codes
        return sum(1 for c in str if c.islower() and (ord(c) % 2) == 0)