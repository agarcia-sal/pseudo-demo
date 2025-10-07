def select_words(s, n):
    result = []
    if s == "":
        return result
    words = []
    start_index = 0
    length_of_s = len(s)
    for index in range(length_of_s):
        if s[index] == " ":
            word_length = index - start_index
            if word_length > 0:
                word = s[start_index:index]
                words.append(word)
            start_index = index + 1
    if start_index < length_of_s:
        word = s[start_index:length_of_s]
        words.append(word)
    vowels = {"a", "e", "i", "o", "u"}
    for word in words:
        n_consonants = sum(1 for letter in word if letter.lower() not in vowels)
        if n_consonants == n:
            result.append(word)
    return result