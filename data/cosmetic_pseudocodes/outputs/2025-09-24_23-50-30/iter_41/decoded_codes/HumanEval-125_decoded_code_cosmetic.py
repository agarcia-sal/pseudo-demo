from typing import List, Union


def split_words(alpha: str) -> Union[int, List[str]]:
    if ' ' not in alpha:
        if ',' not in alpha:
            tally = 0
            for unit in alpha:
                if 'a' <= unit <= 'z' and (ord(unit) % 2 == 0):
                    tally += 1
            return tally
        else:
            beta = ''.join(' ' if x == ',' else x for x in alpha)
            return beta.split(' ')
    else:
        return alpha.split(' ')