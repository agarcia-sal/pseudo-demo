def select_words(s: str, n: int) -> list:
    result = []
    words = []
    index_words = 0
    length_s = len(s)
    current_word = ""
    while index_words < length_s:
        if s[index_words] == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += s[index_words]
        index_words += 1
    if current_word != "":
        words.append(current_word)
    index_word = 0
    length_words = len(words)
    vowels = {"a", "e", "i", "o", "u"}
    while index_word < length_words:
        word = words[index_word]
        n_consonants = 0
        index_char = 0
        length_word = len(word)
        while index_char < length_word:
            char_lower = word[index_char].lower()
            if char_lower not in vowels:
                n_consonants += 1
            index_char += 1
        if n_consonants == n:
            result.append(word)
        index_word += 1
    return result