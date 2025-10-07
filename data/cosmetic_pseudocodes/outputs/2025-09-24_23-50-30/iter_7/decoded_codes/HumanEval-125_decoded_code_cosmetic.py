from typing import List, Union

def split_words(alpha: str) -> Union[List[str], int]:
    if " " in alpha:
        return alpha.split(" ")
    elif "," in alpha:
        delta = alpha.replace(",", " ")
        return delta.split(" ")
    else:
        omega = 0
        for zeta in alpha:
            k = zeta
            if "a" <= k <= "z":
                if ord(k) % 2 == 0:
                    omega += 1
        return omega