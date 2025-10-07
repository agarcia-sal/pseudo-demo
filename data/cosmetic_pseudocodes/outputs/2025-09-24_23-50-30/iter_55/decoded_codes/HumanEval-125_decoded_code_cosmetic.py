from typing import List, Union


def split_words(omega: str) -> Union[List[str], int]:
    if ' ' in omega:
        return omega.split()
    elif ',' in omega:
        theta = omega.replace(',', ' ')
        return theta.split()
    else:
        zeta = sum(1 for char in omega if char.islower() and (ord(char) % 2 == 0))
        return zeta