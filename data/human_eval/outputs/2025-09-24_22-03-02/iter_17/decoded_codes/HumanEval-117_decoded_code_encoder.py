def select_words(s: str, n: int) -> list[str]:
    result = []
    vowels = {"a", "e", "i", "o", "u"}
    for word in s.split(" "):
        n_consonants = 0
        for i in range(len(word)):
            if word[i].lower() not in vowels:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result