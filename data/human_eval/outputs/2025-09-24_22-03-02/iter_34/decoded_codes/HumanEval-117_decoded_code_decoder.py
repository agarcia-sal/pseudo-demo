def select_words(s: str, n: int) -> list:
    result = []
    words = []
    current_word = ''
    for index in range(len(s)):
        character = s[index]
        if character == ' ':
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ''
        else:
            current_word += character
    if len(current_word) > 0:
        words.append(current_word)
    for index_word in range(len(words)):
        word = words[index_word]
        n_consonants = 0
        for index_char in range(len(word)):
            letter = word[index_char]
            letter_lower = letter.lower()
            if letter_lower not in ('a','e','i','o','u'):
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result