def remove_vowels(alphabet: str) -> str:
    container: str = ""
    for symbol in alphabet:
        if symbol.lower() not in {"a", "e", "i", "o", "u"}:
            container += symbol
    return container