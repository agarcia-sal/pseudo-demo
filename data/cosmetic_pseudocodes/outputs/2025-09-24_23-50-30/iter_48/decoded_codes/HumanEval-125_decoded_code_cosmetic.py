from typing import List, Union


def split_words(anchor: str) -> Union[List[str], int]:
    if ' ' not in anchor:
        if ',' in anchor:
            p = anchor.replace(',', ' ')
            return p.split()
        else:
            q = 0
            for s in anchor:
                # Check if s is a lowercase letter a-z and ord(s) is even
                if 'a' <= s <= 'z' and (ord(s) % 2 == 0):
                    q += 1
            return q
    else:
        return anchor.split()