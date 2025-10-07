from typing import List, Dict

def encode(text: str) -> str:
    items: List[str] = list(text.swapcase())
    replacements: Dict[str, str] = {}
    for element in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        replacements[element] = chr(ord(element) + 2)
    result: str = ""
    for index in range(len(items)):
        if items[index] not in replacements:
            result += items[index]
        else:
            result += replacements[items[index]]
    return result