def remove_vowels(str: str) -> str:
    result = ""
    for index in range(1, len(str) + 1):
        char = str[index - 1]
        if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            continue
        result += char
    return result