from typing import List, Union


def split_words(echo: str) -> Union[List[str], int]:
    if ' ' in echo:
        return echo.split()
    elif ',' in echo:
        alpha = echo.replace(',', ' ')
        return alpha.split()
    else:
        omega = [char for char in echo if 'a' <= char <= 'z' and (ord(char) % 2) == 0]
        delta = len(omega)
        return delta