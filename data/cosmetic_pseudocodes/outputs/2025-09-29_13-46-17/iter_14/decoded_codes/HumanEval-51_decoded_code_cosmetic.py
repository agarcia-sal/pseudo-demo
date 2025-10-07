def remove_vowels(text: str) -> str:
    result: str = ""
    index: int = 0
    length: int = len(text)
    vowels = {"a", "e", "i", "o", "u"}
    while index < length:
        ch = text[index]
        if ch.lower() not in vowels:
            result += ch
        index += 1
    return result