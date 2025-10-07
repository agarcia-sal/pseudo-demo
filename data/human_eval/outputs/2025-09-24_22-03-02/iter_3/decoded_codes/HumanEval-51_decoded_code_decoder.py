def remove_vowels(text):
    vowels = set("aeiou")
    return ''.join(c for c in text if c.lower() not in vowels)