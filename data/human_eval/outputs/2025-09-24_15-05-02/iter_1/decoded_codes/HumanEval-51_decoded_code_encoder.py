def remove_vowels(text):
    return ''.join(c for c in text if c.lower() not in ['a', 'e', 'i', 'o', 'u'])