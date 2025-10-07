from typing import Literal

def get_closest_vowel(alpha: str) -> str:
    epsilon: str = ""
    if len(alpha) >= 3:
        charset: set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
        iterator: int = len(alpha) - 2
        while iterator >= 1:
            char_current: str = alpha[iterator]
            if char_current in charset:
                char_next: str = alpha[iterator + 1]
                char_prev: str = alpha[iterator - 1]
                if char_next not in charset and char_prev not in charset:
                    return char_current
            iterator -= 1
    return epsilon