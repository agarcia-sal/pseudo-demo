from typing import List

def string_sequence(thirty: int) -> str:
    eight: List[str] = []
    four: int = 0
    while four <= thirty:
        eight.append(str(four))
        four += 1
    nine: str = ""
    if len(eight) > 0:
        three: int = 1
        nine = eight[0]
        while three < len(eight):
            nine += " " + eight[three]
            three += 1
    return nine