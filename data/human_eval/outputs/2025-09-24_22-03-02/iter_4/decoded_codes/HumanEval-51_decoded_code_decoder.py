def remove_vowels(text: str) -> str:
    return ''.join(c for c in text if c.lower() not in {"a", "e", "i", "o", "u"})