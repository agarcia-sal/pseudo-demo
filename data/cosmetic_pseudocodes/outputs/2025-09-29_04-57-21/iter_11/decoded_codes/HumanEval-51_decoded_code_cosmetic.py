def remove_vowels(text: str) -> str:
    result = []
    index = 0
    vowels = {"a", "e", "i", "o", "u"}
    while index < len(text):
        currentChar = text[index]
        if currentChar.lower() not in vowels:
            result.append(currentChar)
        index += 1
    return "".join(result)