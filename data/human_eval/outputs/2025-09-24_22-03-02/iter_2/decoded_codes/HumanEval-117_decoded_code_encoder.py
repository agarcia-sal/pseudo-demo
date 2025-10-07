def select_words(s: str, n: int) -> list:
    result = []
    for word in s.split():
        n_consonants = 0
        for index in range(len(word)):
            if word[index].lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result