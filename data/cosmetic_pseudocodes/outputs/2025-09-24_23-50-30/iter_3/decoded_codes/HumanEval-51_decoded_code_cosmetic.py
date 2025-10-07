def remove_vowels(inputString: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(ch for ch in inputString if ch.lower() not in vowels)