def select_words(s: str, n: int) -> list:
    result = []
    if s == "":
        return result
    words = s.split()
    for word in words:
        n_consonants = sum(1 for char in word.lower() if char not in "aeiou")
        if n_consonants == n:
            result.append(word)
    return result