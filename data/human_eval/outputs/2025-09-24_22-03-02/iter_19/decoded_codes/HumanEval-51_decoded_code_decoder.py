def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    index = 0
    while index < len(text):
        s = text[index]
        s_lower = s.lower()
        if s_lower not in vowels:
            result += s
        index += 1
    return result