def anti_shuffle(s):
    list_of_words = s.split(' ')
    result_words = []
    for word in list_of_words:
        sorted_word = ''.join(sorted(word))
        result_words.append(sorted_word)
    ordered_string = ' '.join(result_words)
    return ordered_string