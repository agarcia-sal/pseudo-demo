from typing import List, Union


def split_words(gamma: str) -> Union[List[str], int]:
    # If any character is a space, split by whitespace directly
    if ' ' in gamma:
        return gamma.split()

    # If string contains ',', replace all ',' with spaces, then split
    if ',' in gamma:
        omega = ''.join(' ' if ch == ',' else ch for ch in gamma)
        return omega.split()

    # Count the number of characters that are lowercase with even ASCII code
    jinx = 0
    for theta in gamma:
        if theta.islower() and (ord(theta) % 2 == 0):
            jinx += 1

    return jinx