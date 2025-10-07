def select_words(s, n):
    result = [""]
    words = [""]
    temp_word = ""
    index_s = 0
    while index_s < len(s):
        if s[index_s] == " ":
            if temp_word != "":
                words.append(temp_word)
                temp_word = ""
        else:
            temp_word += s[index_s]
        index_s += 1
    if temp_word != "":
        words.append(temp_word)
    index_word = 0
    while index_word < len(words):
        word = words[index_word]
        n_consonants = 0
        index_char = 0
        while index_char < len(word):
            current_char = word[index_char]
            current_char_lower = current_char.lower()
            if current_char_lower not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
            index_char += 1
        if n_consonants == n:
            result.append(word)
        index_word += 1
    return result