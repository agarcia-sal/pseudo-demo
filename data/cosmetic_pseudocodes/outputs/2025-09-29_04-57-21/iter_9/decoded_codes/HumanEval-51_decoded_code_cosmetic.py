def remove_vowels(text: str) -> str:
    result = []
    idx = 0
    while idx < len(text):
        char_current = text[idx]
        if char_current.lower() not in {'a', 'e', 'i', 'o', 'u'}:
            result.append(char_current)
        idx += 1
    return ''.join(result)