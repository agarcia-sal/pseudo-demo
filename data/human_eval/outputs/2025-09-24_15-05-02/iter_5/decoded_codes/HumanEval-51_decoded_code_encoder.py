def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    for character in text:
        if character.lower() not in vowels:
            result_characters.append(character)
    result_string = "".join(result_characters)
    return result_string