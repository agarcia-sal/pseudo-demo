def remove_vowels(text: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    return ''.join(ch for ch in text if ch.lower() not in vowels)