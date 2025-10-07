def remove_vowels(text: str) -> str:
    result = []
    index = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index < len(text):
        current_char = text[index]
        if current_char.lower() not in vowels:
            result.append(current_char)
        index += 1
    return ''.join(result)