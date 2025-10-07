def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    text_length = len(text)
    for index in range(text_length):
        s = text[index]
        s_lower = s.lower()
        if s_lower not in vowels:
            result_characters.append(s)
    result_string = ""
    result_length = len(result_characters)
    for index in range(result_length):
        result_string += result_characters[index]
    return result_string