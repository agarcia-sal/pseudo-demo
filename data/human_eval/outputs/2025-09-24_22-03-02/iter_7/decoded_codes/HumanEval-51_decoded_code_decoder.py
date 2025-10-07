def remove_vowels(TEXT: str) -> str:
    VOWELS = ["a", "e", "i", "o", "u"]
    RESULT = ""
    for CHARACTER in TEXT:
        if CHARACTER.lower() not in VOWELS:
            RESULT += CHARACTER
    return RESULT