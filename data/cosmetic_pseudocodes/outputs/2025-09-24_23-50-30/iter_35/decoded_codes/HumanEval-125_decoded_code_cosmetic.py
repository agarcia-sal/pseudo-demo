from typing import List, Union


def split_words(literal: str) -> Union[List[str], int]:
    if " " in literal:
        return literal.split()
    if "," in literal:
        tmp = literal.replace(",", " ")
        return tmp.split()
    counter = sum(
        1 for c in literal if "a" <= c <= "z" and ord(c) % 2 == 0
    )
    return counter