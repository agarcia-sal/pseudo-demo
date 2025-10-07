def anti_shuffle(s):
    words = s.split(' ')
    ordered_words = []
    for word in words:
        sorted_characters = sorted(word)
        ordered_word = ''.join(sorted_characters)
        ordered_words.append(ordered_word)
    result = ' '.join(ordered_words)
    return result