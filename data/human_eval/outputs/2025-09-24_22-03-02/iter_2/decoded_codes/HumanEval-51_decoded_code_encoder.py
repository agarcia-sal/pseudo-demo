def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for character in text:
        if character.lower() not in vowels:
            result += character
    return result