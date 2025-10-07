def remove_vowels(text: str) -> str:
    result_characters = []
    index = 0
    while index < len(text):
        s = text[index]
        s_lower = s.lower()
        if s_lower != "a" and s_lower != "e" and s_lower != "i" and s_lower != "o" and s_lower != "u":
            result_characters.append(s)
        index += 1
    result = ""
    index = 0
    while index < len(result_characters):
        result += result_characters[index]
        index += 1
    return result