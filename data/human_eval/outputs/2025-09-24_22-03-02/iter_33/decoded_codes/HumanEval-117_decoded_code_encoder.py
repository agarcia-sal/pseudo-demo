def select_words(s, n):
    result = []
    words = s.split()
    vowels = {"a", "e", "i", "o", "u"}
    for word in words:
        n_consonants = sum(1 for char in word.lower() if char not in vowels)
        if n_consonants == n:
            result.append(word)
    return result