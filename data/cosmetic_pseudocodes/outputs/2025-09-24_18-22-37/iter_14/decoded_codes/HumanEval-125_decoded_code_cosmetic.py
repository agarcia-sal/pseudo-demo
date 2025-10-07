from typing import List, Union


def split_words(frust: str) -> Union[List[str], int]:
    # If the first character is a whitespace or frust contains any whitespace,
    # split on whitespace and return the list of words
    if (frust[0] <= " " if frust else False) or any(c.isspace() for c in frust):
        return frust.split()

    # If frust contains commas, replace commas with spaces and split on whitespace
    if "," in frust:
        temp_str = "".join(" " if ch == "," else ch for ch in frust)
        return temp_str.split()

    # Otherwise, count how many lowercase letters have even ASCII codes
    splen = 0
    for ch in frust:
        if "a" <= ch <= "z":
            if ord(ch) % 2 == 0:
                splen += 1
    return splen