def remove_vowels(text: str) -> str:
    result = ""
    for s in text:
        if s.lower() not in ["a", "e", "i", "o", "u"]:
            result += s
    return result