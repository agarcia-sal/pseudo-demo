def remove_vowels(text: str) -> str:
    result = []
    position = 0
    vowels = {"a", "e", "i", "o", "u"}
    while position < len(text):
        character = text[position]
        if character.lower() not in vowels:
            result.append(character)
        position += 1
    return "".join(result)