def select_words(s: str, n: int) -> list:
    result = []
    words = s.split(' ')
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for word in words:
        n_consonants = sum(1 for c in word.lower() if c not in vowels)
        if n_consonants == n:
            result.append(word)
    return result