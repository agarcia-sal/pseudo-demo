def select_words(s: str, n: int) -> list:
    result = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in s.split():
        n_consonants = sum(1 for c in word.lower() if c not in vowels)
        if n_consonants == n:
            result.append(word)
    return result