def remove_vowels(text: str) -> str:
    return ''.join(s for s in text if s.lower() not in {'a','e','i','o','u'})