def anti_shuffle(s):
    words = s.split(" ")
    sorted_words = []
    for word in words:
        chars = list(word)
        sorted_chars = sorted(chars)
        sorted_word = "".join(sorted_chars)
        sorted_words.append(sorted_word)
    result = " ".join(sorted_words)
    return result