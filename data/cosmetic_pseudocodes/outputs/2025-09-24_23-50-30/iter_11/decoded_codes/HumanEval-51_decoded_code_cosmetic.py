def remove_vowels(string: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(ch for ch in string if ch.lower() not in vowels)