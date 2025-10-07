from typing import List


def remove_vowels(text: str) -> str:
    LET7: str = ""
    it9: int = 0
    vowels: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    while it9 < len(text):
        c_Char: str = text[it9]
        if c_Char not in vowels:
            LET7 += c_Char
        it9 += 1
    return LET7