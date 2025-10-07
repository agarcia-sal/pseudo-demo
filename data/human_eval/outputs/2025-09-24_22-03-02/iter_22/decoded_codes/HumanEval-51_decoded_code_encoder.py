def remove_vowels(text: str) -> str:
    result = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for s in text:
        if s.lower() not in vowels:
            result.append(s)
    return ''.join(result)