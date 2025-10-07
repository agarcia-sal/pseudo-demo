def select_words(s: str, n: int) -> list:
    result = []
    if s == "":
        return result
    words = []
    current_word = ""
    for i in range(len(s)):
        if s[i] == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += s[i]
    if current_word != "":
        words.append(current_word)
    for word in words:
        n_consonants = 0
        for k in range(len(word)):
            lower_char = word[k].lower()
            if lower_char not in "aeiou":
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result