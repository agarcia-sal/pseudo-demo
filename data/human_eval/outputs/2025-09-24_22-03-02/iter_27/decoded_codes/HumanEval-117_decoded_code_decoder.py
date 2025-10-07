def select_words(s, n):
    result = []
    if s == "":
        return result
    words = []
    current_word = ""
    length_s = len(s)
    index_s = 0
    while index_s < length_s:
        char = s[index_s]
        if char == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
        index_s += 1
    if current_word != "":
        words.append(current_word)
    index_words = 0
    length_words = len(words)
    while index_words < length_words:
        word = words[index_words]
        n_consonants = 0
        length_word = len(word)
        index_word = 0
        while index_word < length_word:
            letter = word[index_word]
            letter_lower = letter.lower()
            if letter_lower != "a" and letter_lower != "e" and letter_lower != "i" and letter_lower != "o" and letter_lower != "u":
                n_consonants += 1
            index_word += 1
        if n_consonants == n:
            result.append(word)
        index_words += 1
    return result