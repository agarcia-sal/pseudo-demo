from typing import List, Union


def split_words(alpha: str) -> Union[List[str], int]:
    if ' ' not in alpha and ',' in alpha:
        beta = ''.join(' ' if c == ',' else c for c in alpha)
        return beta.split()
    elif ' ' in alpha:
        return alpha.split()
    else:
        gamma = 0
        for epsilon in alpha:
            if epsilon.islower() and (ord(epsilon) % 2) == 0:
                gamma += 1
        return gamma