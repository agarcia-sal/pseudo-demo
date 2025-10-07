def remove_vowels(text: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for char in text:
        if char.lower() not in vowels:
            result.append(char)
    return ''.join(result)