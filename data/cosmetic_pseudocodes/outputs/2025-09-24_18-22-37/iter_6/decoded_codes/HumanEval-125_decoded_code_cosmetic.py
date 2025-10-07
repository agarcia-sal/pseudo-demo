from typing import Union, List


def split_words(alpha: str) -> Union[int, List[str]]:
    if ' ' not in alpha:
        if ',' not in alpha:
            counter: int = 0
            for current_char in alpha:
                if 'a' <= current_char <= 'z':
                    ascii_val = ord(current_char)
                    if ascii_val % 2 == 0:
                        counter += 1
            return counter
        replaced_string: str = alpha.replace(',', ' ')
        return replaced_string.split()
    return alpha.split()