from typing import List

def encrypt(text: str) -> str:
    letters: str = "abcdefghijklmnopqrstuvwxyz"
    result: List[str] = []
    i: int = 0
    while i < len(text):
        ch: str = text[i]
        pos: int = letters.find(ch)
        if pos != -1:
            new_pos: int = (pos + 4) % 26
            result.append(letters[new_pos])
        else:
            result.append(ch)
        i += 1
    return "".join(result)