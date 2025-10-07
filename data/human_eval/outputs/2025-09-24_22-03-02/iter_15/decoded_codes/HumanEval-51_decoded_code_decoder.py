def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    for s in text:
        if s.lower() not in vowels:
            result_characters.append(s)
    result_string = "".join(result_characters)
    return result_string