def remove_vowels(text):
    result = []
    for character in text:
        if character.lower() not in ["a", "e", "i", "o", "u"]:
            result.append(character)
    return "".join(result)