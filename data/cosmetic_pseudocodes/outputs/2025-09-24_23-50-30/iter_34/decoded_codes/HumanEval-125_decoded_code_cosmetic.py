from typing import Union, List


def split_words(delta: str) -> Union[List[str], int]:
    if ' ' in delta:
        return delta.split(' ')
    elif ',' in delta:
        omega = delta.replace(',', ' ')
        return omega.split(' ')
    else:
        mu = [z for z in delta if z.islower() and (ord(z) % 2 == 0)]
        return len(mu)