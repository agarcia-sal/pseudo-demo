def select_words(s: str, n: int) -> list:
    result = []
    if s == "":
        return result
    for index_word in range(len(s.split()) ):
        word = s.split()[index_word]
        n_consonants = 0
        for i in range(len(word)):
            letter = word[i]
            if letter.lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result