def select_words(s: str, n: int) -> list[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    for word in s.split():
        n_consonants = sum(1 for c in word if c.lower() not in vowels)
        if n_consonants == n:
            result.append(word)
    return result