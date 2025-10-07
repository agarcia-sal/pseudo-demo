def select_words(s: str, n: int) -> list[str]:
    result = [""]
    if s == "":
        return result
    words = []
    current_word = ""
    length_s = len(s)
    for index in range(length_s):
        if s[index] == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += s[index]
    if current_word != "":
        words.append(current_word)
    for word in words:
        n_consonants = 0
        length_word = len(word)
        for char_index in range(length_word):
            current_char = word[char_index]
            char_lower = current_char.lower()
            if char_lower not in {"a", "e", "i", "o", "u"}:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result