def select_words(s: str, n: int) -> list:
    result = []
    splitted_words = []
    current_word = ''
    s_length = len(s)
    for index in range(s_length):
        current_character = s[index]
        if current_character == ' ':
            if len(current_word) > 0:
                splitted_words.append(current_word)
                current_word = ''
        else:
            current_word += current_character
    if len(current_word) > 0:
        splitted_words.append(current_word)
    for word in splitted_words:
        n_consonants = 0
        word_length = len(word)
        for i in range(word_length):
            current_letter = word[i]
            lower_letter = current_letter.lower()
            if lower_letter not in {'a', 'e', 'i', 'o', 'u'}:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result